import json

from django.contrib.postgres.fields import JSONField
from django.db import models

from kubernetes import client
from kubernetes.client.rest import ApiException

PULL_POLICY = [
    'Always',
    'IfNotPresent',
    'Never'
]

RESTART_POLICY = [
    'Always',
    'OnFailure',
    'Never'
]



class KubernetesBase(models.Model):
    id = models.UUIDField(default=uuid4, editable=False, primary_key=True)
    name = models.CharField(max_length=128, default="kubernetes-object")
    description = models.CharField(max_length=128, null=True, blank=True)
    cluster = models.ForeignKey('TargetCluster', on_delete=models.SET_NULL, null=True)
    config = models.JSONField(default=dict, null=True, blank=True)
    class Meta:
        abstract = True



class KubernetesVolume(KubernetesBase):

    def get_obj(self):
        return client.V1Volume(
            name=self.name,
            empty_dir={}
        )



class KubernetesVolumeMount(KubernetesBase):
    mount_path = models.CharField(max_length=255, default="/media")
    sub_path = models.CharField(max_length=255, default=None, null=True, blank=True)

    def get_obj(self):
        return client.V1VolumeMount(
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
        return client.V1Container(
            name = self.name,
            image = ':'.join(self.image_name, self.image_tag),
            image_pull_policy = self.image_pull_policy,
            ports = [client.V1ContainerPort(container_port=self.port)],
            volume_mounts = [self.volume_mount.get_obj()],
            command = [self.command],
            args = [self.args.split(",")]
        )



class KubernetesMetadataObjBase(KubernetesBase):
    labels = models.JSONField(default={'app': 'default'})
    annotations = models.JSONFIELD(default=dict, null=True, blank=True)

    class Meta:
        abstract = True



class KubernetesPodTemplate(KubernetesMetadataObjBase):
    volume = models.ForeignKey('KubernetesVolume', null=True, blank=True, on_delete=models.SET_NULL)
    primary_container = models.ForeignKey('KubernetesContainer', on_delete=models.CASCADE, related_name='primary_container')
    secondary_container = models.ForeignKey('KubernetesContainer', null=True, blank=True, on_delete=models.SET_NULL, related_name='secondary_container')
    restart_policy = models.CharField(max_length=16, choices=RESTART_POLICY, default='Never')

    def get_obj(self):
        return client.V1PodTemplateSpec(
            metadata=client.V1ObjectMeta(
                labels=json.loads(self.labels),
                annotations=json.loads(self.annotations)
            ),
            spec=client.V1PodSpec(
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
    target_port = models.IntegerField(default=80)

    class Meta:
        abstract= True



class KubernetesService(KubernetesNetworkingBase):
    selector = models.JSONField(default=dict)
    port = models.IntegerField(default=80)

    def get_obj(self):
        return client.V1Service(
            api_version = self.api_version,
            kind = self.kind,
            metadata=client.V1ObjectMeta(
                labels=json.loads(self.labels),
                annotations=json.loads(self.annotations)
            ),
            spec=client.V1ServiceSpec(
                selector = self.selector,
                ports = [client.V1ServicePort(
                    port=self.port,
                    target_port=self.target_port
                )]
            )
        )



class KubernetesIngress(KubernetesNetworkingBase):
    hostname = models.CharField(max_length=255, default="localhost")
    path = models.CharField(max_length=255, default="/")
    target_service = models.ForeignKey('KubernetesService', )
