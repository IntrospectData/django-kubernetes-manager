import contextlib
import json

from django.contrib.postgres.fields import JSONField
from django.db import models

from uuid import uuid4
from kubernetes import client, config

PULL_POLICY = [
    ('Always', 'Always'),
    ('IfNotPresent', 'IfNotPresent'),
    ('Never', 'Never')
]

RESTART_POLICY = [
    ('Always', 'Always'),
    ('OnFailure', 'OnFailure'),
    ('Never', 'Never')
]



class KubernetesBase(models.Model):
    id = models.UUIDField(default=uuid4, editable=False, primary_key=True)
    name = models.CharField(max_length=128, default="kubernetes-object")
    description = models.CharField(max_length=128, null=True, blank=True)
    cluster = models.ForeignKey('TargetCluster', on_delete=models.SET_NULL, null=True)
    config = JSONField(default=dict, null=True, blank=True)

    class Meta:
        abstract = True

    @contextlib.contextmanager
    def get_client(self, API=client.CoreV1Api, **kwargs):
        """Gets a k8s api client based on the credential associated with this JobInstance

            Args:
                API (client.<type>) - Kubernetes Client Type
            Returns:
                object of type <API>
        """
        if "persist_config" not in kwargs:
            kwargs["persist_config"] = False
        with NamedTemporaryFile() as ntf:
            kwargs["config_file"] = ntf.name
            if isinstance(self.cluster.config, dict):
                cc = json.dumps(self.cluster.config)
            else:
                cc = self.cluster.config
            with open(ntf.name, "w") as f:
                f.write(cc)
            yield API(api_client=config.new_client_from_config(**kwargs))

    client = property(get_client)



class KubernetesVolume(KubernetesBase):

    def get_obj(self):
        return self.client.V1Volume(
            name=self.name,
            empty_dir={}
        )



class KubernetesVolumeMount(KubernetesBase):
    mount_path = models.CharField(max_length=255, default="/media")
    sub_path = models.CharField(max_length=255, default=None, null=True, blank=True)

    def get_obj(self):
        return self.client.V1VolumeMount(
            name=self.name,
            mount_path=self.mount_path,
            sub_path=slef.sub_path
        )



class KubernetesContainer(KubernetesBase):
    image_name = models.CharField(max_length=200, db_index=True, help_text="Properly qualified image name to execute this job within", default="debian")
    image_tag = models.CharField(max_length=100, db_index=True, help_text="Tag name for the image to be used for this job", default="latest")
    image_pull_policy = models.CharField(max_length=16, choices=PULL_POLICY, default='IfNotPresent')
    command = models.TextField(help_text="Command to run when instantiating container", null=True, blank=True, default="/bin/sh")
    args = models.TextField(help_text="Comma separated args to run with command when instantiating container.", null=True, blank=True, default="-c,sleep 6000")
    port = models.IntegerField(default=80)
    volume_mount = models.ForeignKey('KubernetesVolumeMount', null=True, blank=True, on_delete=models.SET_NULL)

    def get_obj(self):
        return self.client.V1Container(
            name = self.name,
            image = ':'.join(self.image_name, self.image_tag),
            image_pull_policy = self.image_pull_policy,
            ports = [self.client.V1ContainerPort(container_port=self.port)],
            volume_mounts = [self.volume_mount.get_obj()],
            command = [self.command],
            args = [self.args.split(",")]
        )



class KubernetesMetadataObjBase(KubernetesBase):
    labels = JSONField(default=dict)
    annotations = JSONField(default=dict, null=True, blank=True)

    class Meta:
        abstract = True



class KubernetesPodTemplate(KubernetesMetadataObjBase):
    volume = models.ForeignKey('KubernetesVolume', null=True, blank=True, on_delete=models.SET_NULL)
    primary_container = models.ForeignKey('KubernetesContainer', on_delete=models.CASCADE, related_name='primary_container')
    secondary_container = models.ForeignKey('KubernetesContainer', null=True, blank=True, on_delete=models.SET_NULL, related_name='secondary_container')
    restart_policy = models.CharField(max_length=16, choices=RESTART_POLICY, default='Never')

    def get_obj(self):
        return self.client.V1PodTemplateSpec(
            metadata=self.client.V1ObjectMeta(
                labels=json.loads(self.labels),
                annotations=json.loads(self.annotations)
            ),
            spec=self.client.V1PodSpec(
                volumes=[self.volume.get_obj()],
                containers=[
                    self.primary_container.get_obj(),
                    self.secondary_container.get_obj()
                ] if self.secondary_container is not None else [self.primary_container.get_obj()],
                restart_policy = self.restart_policy
            )
        )




class KubernetesNetworkingBase(KubernetesMetadataObjBase):
    api_version = models.CharField(max_length=16, default="v1")
    kind = models.CharField(max_length=16, default="Service")
    port = models.IntegerField(default=80)

    class Meta:
        abstract= True



class KubernetesDeployment(KubernetesNetworkingBase):
    selector = JSONField(default=dict)
    replicas = models.IntegerField(default=1)
    pod_template = models.ForeignKey('KubernetesPodTemplate', on_delete=models.CASCADE)

    def get_obj(self):
        return self.client.V1Deployment(
            api_version=self.api_version,
            kind=self.kind,
            metadata=self.client.V1ObjectMeta(
                labels=json.loads(self.labels),
                annotations=json.loads(self.labels)
            ),
            spec=self.client.V1DeploymentSpec(
                selector=json.loads(self.selector),
                replicas=self.replicas,
                template=self.pod_template.get_obj()
            )
        )



class KubernetesService(KubernetesNetworkingBase):
    selector = JSONField(default=dict)
    target_port = models.IntegerField(default=80)
    def get_obj(self):
        return self.client.V1Service(
            api_version = self.api_version,
            kind = self.kind,
            metadata=self.client.V1ObjectMeta(
                labels=json.loads(self.labels),
                annotations=json.loads(self.annotations)
            ),
            spec=self.client.V1ServiceSpec(
                selector = json.loads(self.selector),
                ports = [self.client.V1ServicePort(
                    port=self.port,
                    target_port=self.target_port
                )]
            )
        )



class KubernetesIngress(KubernetesNetworkingBase):
    hostname = models.CharField(max_length=255, default="localhost")
    path = models.CharField(max_length=255, default="/")
    target_service = models.ForeignKey('KubernetesService', on_delete=models.CASCADE)

    def get_obj(self):
        return self.client.NetworkingV1beta1Ingress(
            api_version=self.api_version,
            kind=self.kind,
            metadata=self.client.V1ObjectMeta(
                name=self.name,
                annotations=self.annotations
            ),
            spec=self.client.NetworkingV1beta1IngressSpec(
                rules=[self.client.NetworkingV1beta1IngressRule(
                    host=self.hostname,
                    http=self.client.NetworkingV1beta1HTTPIngressRuleValue(
                        paths=[self.client.NetworkingV1beta1HTTPIngressPath(
                            path=self.path,
                            backend=self.client.NetworkingV1beta1IngressBackend(
                                service_port=self.target_service.port,
                                service_name=self.target_service.name
                            )
                        )]
                    )
                )]
            )
        )
