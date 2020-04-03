import json
import re
from tempfile import NamedTemporaryFile
from time import sleep
from uuid import uuid4

from django.contrib.postgres.fields import JSONField
from django.db import models

from django_extensions.db.models import TitleSlugDescriptionModel
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

byte_units = {
    "E": 1000**6, "P": 1000**5, "T": 1000**4,
    "G": 1000**3, "M": 1000**2, "K": 1000,
    "Ei": 1024**6, "Pi": 1024**5, "Ti": 1024**4,
    "Gi": 1024**3, "Mi": 1024**2, "Ki": 1024
}



class KubernetesTelemetryMixin(models.Model):
    """
    KubernetesTelemetryMixin
    :type: mixin
    :description: Extends child model to include telemetry features.
    :inherits: django.db.models.Model
    :fields: object_status, average_cpu_usage,
        average_mem_usage, cpu_usage_seconds, mem_usage_seconds
    """
    object_status = models.CharField(max_length=128, null=True, blank=True,
        help_text="status of the object in Kubernetes"
    )
    average_cpu_usage = models.DecimalField(null=True, blank=True, max_digits=8,
        decimal_places=4, help_text="Average PIT CPU units consumed"
    )
    average_mem_usage = models.IntegerField(null=True, blank=True,
        help_text="Average PIT bytes consumed")
    cpu_usage_seconds = models.DecimalField(null=True, blank=True, max_digits=8,
        decimal_places=4, help_text="Average cpu usage * seconds live")
    )
    mem_usage_seconds = models.IntegerField(null=True, blank=True,
        help_text="Average mem usage * seconds live")

    class Meta:
        abstract = True

    def splitNumeric(self, size):
        """
        :description: Parses string into numeric component.
        """
        return filter(None, re.split(r'(\d+)', size))

    def parseSize(self, size):
        """
        :description: Parses string as numeric, suffix and converts to bytes.
        """
        number, unit = [string for string in self.splitNumeric(size)]
        return int(float(number)*byte_units[unit])

    def read_pod_metrics(self):
        """
        :description: Uses metrics_server to get  cadvisor data.
        """
        api_instance = self.get_client(API=client.CustomObjectsApi)
        pod_name = self.slug
        pod_namespace = self.namespace
        items = api_instance.list_cluster_custom_object('metrics.k8s.io',
            'v1beta1', 'pods').get("items", [])
        return [pod for pod in items if pod_name in pod.get("metadata", {}
            ).get("name") and pod_namespace in pod.get("metadata", {}
                ).get("namespace")]

    def read_pod_usage(self):
        """
        :description: Converts metrics into dictionary for api usage.
        """
        pod_name = self.pod_template.slug
        pod_namespace = self.namespace
        pod_metrics = self.read_pod_metrics()
        cpu = 0.000
        memory = 0
        for metric in pod_metrics:
            for container in metric.get("containers", []):
                ccpu = container.get("usage", {}).get("cpu", None)
                cmem = container.get("usage", {}).get("memory", None)
                if 'm' in ccpu:
                    ccpu = int(ccpu.split("m")[0]) / 1000.000
                else:
                    ccpu = int(ccpu)
                cpu += ccpu
                memory += self.parseSize(cmem)
        return {'cpu': cpu, 'memory': memory}

    def status(self):
        """
        :description: Returns status data of object.
        """
        type = self._meta.model_name
        name = self.slug
        namespace = self.namespace.slug
        api_instance = self.get_client(API=client.ExtensionsV1beta1Api)
        if type == 'kubernetesjob':
            api_response = api_instance.read_namespaced_job_status(
                name, namespace)
        if type == 'kubernetesdeployment':
            api_response = api_instance.read_namespaced_deployment_status(
                name, namespace)
        return api_response.status

class KubernetesBase(TitleSlugDescriptionModel):
    """
    KubernetesBase
    :type: model (abstract)
    :description: Base parent model that all subsequent models inherit from.
    :inherits: django_extensions.db.models.TitleSlugDescriptionModel
    :fields: id, cluster, config, deployed, deleted
    """
    id = models.UUIDField(default=uuid4, editable=False, primary_key=True)
    cluster = models.ForeignKey('TargetCluster', on_delete=models.SET_NULL,
        null=True
    )
    config = JSONField(default=dict, null=True, blank=True)
    deployed = models.DateTimeField(null=True, blank=True)
    deleted = models.DateTimeField(null=True, blank=True)


    class Meta:
        abstract = True

    def slugify_function(self, content):
        """
        :description: Overrides default slugify with custom logic.
        """
        return self.title.replace("_", "-").replace(" ", "-").lower()

    def get_client(self, API=client.CoreV1Api, **kwargs):
        """Gets a k8s api client

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
            return API(api_client=config.new_client_from_config(
                config_file=ntf.name)
            )



class KubernetesMetadataObjBase(KubernetesBase):
    """
    KubernetesMetadataObjBase
    :type: model (abstract)
    :description: Extends KubernetesBase to include metadata fields.
    :inherits: django_kubernetes_manager.models.base.KubernetesBase
    :fields: labels, annotations
    """
    labels = JSONField(default=dict)
    annotations = JSONField(default=dict, null=True, blank=True)

    class Meta:
        abstract = True



class KubernetesNetworkingBase(KubernetesMetadataObjBase):
    """
    KubernetesNetworkingBase
    :type: model (abstract)
    :description: Extends KubernetesMetadataObjBase to include network fields.
    :inherits: django_kubernetes_manager.models.base.KubernetesMetadataObjBase
    :fields: labels, annotations
    """
    api_version = models.CharField(max_length=16, default="v1")
    kind = models.CharField(max_length=16)
    port = models.IntegerField(default=80)
    namespace = models.CharField(max_length=64, default="default")
    kuid = models.CharField(max_length=48, null=True, blank=True,
        help_text="Object's UID in the cluster"
    )

    class Meta:
        abstract= True



class KubernetesNamespace(KubernetesMetadataObjBase):
    """
    KubernetesNetworkingBase
    :type: model
    :description: Holds data related to a Kubernetes namespace.
    :inherits: django_kubernetes_manager.models.base.KubernetesMetadataObjBase
    :fields: api_version, kind, exists
    """
    api_version = models.CharField(max_length=16, default="v1")
    kind = models.CharField(max_length=16, default="Namespace")
    exists = models.BooleanField(default=False)

    def get_obj(self):
        """
        :description: Generate namespace spec.
        """
         return client.V1Namespace(
            api_version = self.api_version,
            kind = self.kind,
            metadata=client.V1ObjectMeta(
                name = self.slug,
                labels=self.labels,
                annotations=self.annotations
            ),
            spec = client.V1NamespaceSpec()
         )

    def deploy(self):
        """
        :description: Deploy namespace obj.
        """
        api_instance = self.get_client(API=client.CoreV1Api)
        body = self.get_obj()
        api_response = api_instance.create_namespace(
            body = body,
        )
        self.exists = True
        self.save()
        return str(api_response.status)

    def remove(self):
        """
        :description: Delete namespace from cluster.
        """
        api_instance = self.get_client(API=client.CoreV1Api)
        api_response = api_instance.delete_namespace(
            name = self.slug,
        )
        self.exists = False
        self.save()
        return str(api_response.status)



class KubernetesVolume(KubernetesBase):
    """
    KubernetesVolume
    :type: model
    :description: Holds data related to a kubernetes volume.
    :inherits: django_kubernetes_manager.models.base.KubernetesBase
    :fields: *
    """
    def get_obj(self):
        """
        :description: Generate volume spec.
        """
        if self.config.get("configmap"):
            return client.V1Volume(
                name=self.slug,
                config_map=client.V1ConfigMapVolumeSource(
                    name = self.config.get("configmap")
                )
            )
        return client.V1Volume(
            name=self.slug,
            empty_dir=client.V1EmptyDirVolumeSource()
        )



class KubernetesVolumeMount(KubernetesBase):
    """
    KubernetesVolumeMount
    :type: model
    :description: Holds data related to a kubernetes volume mount.
    :inherits: django_kubernetes_manager.models.base.KubernetesBase
    :fields: mount_path, sub_path
    """
    mount_path = models.CharField(max_length=255, default="/media")
    sub_path = models.CharField(max_length=255, default=None, null=True,
        blank=True
    )

    def get_obj(self):
        """
        :description: Generate mount spec.
        """
        return client.V1VolumeMount(
            name=self.slug,
            mount_path=self.mount_path,
            sub_path=self.sub_path
        )



class KubernetesContainer(KubernetesBase):
    """
    KubernetesContainer
    :type: model
    :description: Holds data related to a kubernetes contaienr.
    :inherits: django_kubernetes_manager.models.base.KubernetesBase
    :fields: image_name, image_tag, image_pull_policy, command, args, port,
        volume_mount
    """
    image_name = models.CharField(max_length=200, db_index=True,
        help_text="Properly qualified image name.",
        default="debian"
    )
    image_tag = models.CharField(max_length=100, db_index=True,
        help_text="Tag name for the image to be used for this job",
        default="latest"
    )
    image_pull_policy = models.CharField(max_length=16, choices=PULL_POLICY,
        default='IfNotPresent'
    )
    command = models.TextField(help_text="Command to run when start container",
        null=True, blank=True
    )
    args = models.TextField(help_text="Comma separated args to run with command\
        when instantiating container.", null=True, blank=True
    )
    port = models.IntegerField(default=80)
    volume_mount = models.ForeignKey('KubernetesVolumeMount', null=True,
        blank=True, on_delete=models.SET_NULL)

    def get_obj(self):
        """
        :description: Generate container spec.
        """
        return client.V1Container(
            name = self.slug,
            image = ':'.join([self.image_name, self.image_tag]),
            image_pull_policy = self.image_pull_policy,
            ports = [client.V1ContainerPort(container_port=self.port)],
            volume_mounts = [
                self.volume_mount.get_obj()
            ] if self.volume_mount is not None else None,
            command = [self.command],
            args = self.args.split(",")
        )



class KubernetesConfigMap(KubernetesMetadataObjBase):
    """
    KubernetesConfigMap
    :type: model
    :description: Holds data related to a kubernetes volume mount.
    :inherits: django_kubernetes_manager.models.base.KubernetesMetadataObjBase
    :fields: kind, data, binary, override_name, namespace
    """
    kind = models.CharField(max_length=16, default="ConfigMap")
    data = JSONField(default=dict, null=True, blank=True)
    binary = models.BinaryField(null=True, blank=True)
    override_name = models.CharField(max_length=32, null=True, blank=True,
        default="ConfigMap"
    )
    namespace = models.CharField(max_length=64, default="default")

    def get_obj(self):
        """
        :description: Generate configmap spec.
        """
        return client.V1ConfigMap(
            metadata=client.V1ObjectMeta(
                name = self.slug,
                labels=self.labels,
                annotations=self.annotations
            ),
            kind = self.kind,
            data = self.data if self.data else None,
            binary_data = {
                str(self.override_name): self.binary
            } if self.binary else None
        )

    def deploy(self):
        """
        :description: Deploy configmap obj.
        """
        api_instance = self.get_client(API=client.CoreV1Api)
        body = self.get_obj()
        api_response = api_instance.create_namespaced_config_map(
            body = body,
            namespace = self.namespace
        )
        self.kuid = api_response.metadata.uid
        self.save()
        return str(api_response.status)

    def remove(self):
        """
        :description: Delete configmap from namespace.
        """
        api_instance = self.get_client(API=client.CoreV1Api)
        api_response = api_instance.delete_namespaced_config_map(
            name = self.slug,
            namespace = self.namespace
        )
        self.kuid = None
        self.save()
        return str(api_response.status)



class KubernetesPodTemplate(KubernetesMetadataObjBase):
    """
    KubernetesPodTemplate
    :type: model
    :description: Holds data related to a kubernetes pod spec.
    :inherits: django_kubernetes_manager.models.base.KubernetesMetadataObjBase
    :fields: volume, primary_container, secondary_container, restart_policy
    """
    volume = models.ForeignKey('KubernetesVolume', null=True, blank=True,
        on_delete=models.SET_NULL
    )
    primary_container = models.ForeignKey('KubernetesContainer',
        on_delete=models.CASCADE, related_name='primary_container'
    )
    secondary_container = models.ForeignKey('KubernetesContainer', null=True,
        blank=True, on_delete=models.SET_NULL,
        related_name='secondary_container'
    )
    restart_policy = models.CharField(max_length=16, choices=RESTART_POLICY,
        default='Never'
    )

    def get_obj(self):
        """
        :description: Generate pod spec.
        """
        return client.V1PodTemplateSpec(
            metadata=client.V1ObjectMeta(
                name = self.slug,
                labels=self.labels,
                annotations=self.annotations
            ),
            spec=client.V1PodSpec(
                volumes=[
                    self.volume.get_obj()
                ] if self.volume is not None else None,
                containers=[
                    self.primary_container.get_obj(),
                    self.secondary_container.get_obj()
                ] if self.secondary_container is not None else [
                    self.primary_container.get_obj()
                ],
                restart_policy = self.restart_policy
            )
        )



class KubernetesDeployment(KubernetesNetworkingBase, KubernetesTelemetryMixin):
    """
    KubernetesDeployment
    :type: model
    :description: Holds data related to a kubernetes deployment.
    :inherits: django_kubernetes_manager.models.base.KubernetesNetworkingBase,
        django_kubernetes_manager.models.base.KubernetesTelemetryMixin
    :fields: selector, replicas, pod_template
    """
    selector = JSONField(default=dict)
    replicas = models.IntegerField(default=1)
    pod_template = models.ForeignKey('KubernetesPodTemplate',
        on_delete=models.CASCADE
    )

    def get_obj(self):
        """
        :description: Generate Deployment spec.
        """
        return client.V1Deployment(
            api_version=self.api_version,
            kind=self.kind,
            metadata=client.V1ObjectMeta(
                name = self.slug,
                labels=self.labels,
                annotations=self.annotations
            ),
            spec=client.V1DeploymentSpec(
                selector=client.V1LabelSelector(match_labels=self.selector),
                replicas=self.replicas,
                template=self.pod_template.get_obj()
            )
        )

    def deploy(self):
        """
        :description: Deploy deployment obj.
        """
        api_instance = self.get_client(API=client.AppsV1Api)
        body = self.get_obj()
        api_response = api_instance.create_namespaced_deployment(
            body = body,
            namespace = self.namespace
        )
        ticker = 0
        while self.status().unavailable_replicas > 0:
            if ticker >= self.config.get("timeout", 60):
                raise Exception(
                    'Timeout: no replicas available after {} ticks'.format(
                        str(ticker)
                    )
                )
            ticker +=1
            sleep(1)
        self.kuid = api_response.metadata.uid
        self.save()
        return str(api_response.status)

    def remove(self):
        """
        :description: Remove deployment from namespace.
        """
        api_instance = self.get_client(API=client.AppsV1Api)
        api_response = api_instance.delete_namespaced_deployment(
            name = self.slug,
            namespace = self.namespace
        )
        self.kuid = None
        self.save()
        return str(api_response.status)



class KubernetesJob(KubernetesNetworkingBase, KubernetesTelemetryMixin):
    """
    KubernetesJob
    :type: model
    :description: Holds data related to a kubernetes pod spec.
    :inherits: django_kubernetes_manager.models.base.KubernetesNetworkingBase,
        django_kubernetes_manager.models.base.KubernetesTelemetryMixin
    :fields: selector, replicas, pod_template
    """
    pod_template = models.ForeignKey('KubernetesPodTemplate',
        on_delete=models.CASCADE
    )
    backoff_limit = models.IntegerField(default=3)

    def get_obj(self):
        """
        :description: Generate job spec.
        """
        return client.V1Job(
            api_version=self.api_version,
            kind=self.kind,
            metadata=client.V1ObjectMeta(
                name = self.slug,
                labels = self.labels,
                annotations = self.annotations
            ),
            spec=client.V1JobSpec(
                template=self.pod_template.get_obj(),
                backoff_limit=self.backoff_limit,
                ttl_seconds_after_finished = 10
            )
        )

    def deploy(self):
        """
        :description: Deploy job to ns.
        """
        api_instance = self.get_client(API=client.BatchV1Api)
        body = self.get_obj()
        api_response = api_instance.create_namespaced_job(
            body = body,
            namespace = self.namespace
        )
        self.kuid = api_response.metadata.uid
        self.save()
        return str(api_response.status)

    def remove(self):
        """
        :description: Remove job from ns.
        """
        api_instance = self.get_client(API=client.BatchV1Api)
        api_response = api_instance.delete_namespaced_job(
            name = self.slug,
            namespace = self.namespace
        )
        self.kuid = None
        self.save()
        return str(api_response.status)



class KubernetesService(KubernetesNetworkingBase):
    """
    KubernetesService
    :type: model
    :description: Holds data related to a kubernetes service.
    :inherits: django_kubernetes_manager.models.base.KubernetesNetworkingBase
    :fields: selector, target_port
    """
    selector = JSONField(default=dict)
    target_port = models.IntegerField(default=80)

    def get_obj(self):
        """
        :description: Generate service spec.
        """
        return client.V1Service(
            api_version = self.api_version,
            kind = self.kind,
            metadata=client.V1ObjectMeta(
                name = self.slug,
                labels=self.labels,
                annotations=self.annotations
            ),
            spec=client.V1ServiceSpec(
                selector = client.V1LabelSelector(match_labels=self.selector),
                ports = [client.V1ServicePort(
                    port=self.port,
                    target_port=self.target_port
                )]
            )
        )

    def deploy(self):
        """
        :description: Deploy service to ns.
        """
        api_instance = self.get_client(API=client.ExtensionsV1beta1Api)
        body = self.get_obj()
        api_response = api_instance.create_namespaced_service(
            body = body,
            namespace = self.namespace
        )
        self.kuid = api_response.metadata.uid
        self.save()
        return str(api_response.status)

    def remove(self):
        """
        :description: Remove service from ns.
        """
        api_instance = self.get_client(API=client.ExtensionsV1beta1Api)
        api_response = api_instance.delete_namespaced_service(
            name = self.slug,
            namespace = self.namespace
        )
        self.kuid = None
        self.save()
        return str(api_response.status)



class KubernetesIngress(KubernetesNetworkingBase):
    """
    KubernetesIngress
    :type: model
    :description: Holds data related to a kubernetes ingress.
    :inherits: django_kubernetes_manager.models.base.KubernetesNetworkingBase
    :fields: hostname, path, target_service
    """
    hostname = models.CharField(max_length=255, default="localhost")
    path = models.CharField(max_length=255, default="/")
    target_service = models.ForeignKey('KubernetesService',
        on_delete=models.CASCADE
    )

    def get_obj(self):
        """
        :description: Generate ingress obj.
        """
        return client.NetworkingV1beta1Ingress(
            api_version=self.api_version,
            kind=self.kind,
            metadata=client.V1ObjectMeta(
                name=self.slug,
                annotations=self.annotations
            ),
            spec=client.NetworkingV1beta1IngressSpec(
                selector = client.V1LabelSelector(match_labels=self.selector),
                rules=[client.NetworkingV1beta1IngressRule(
                    host=self.hostname,
                    http=client.NetworkingV1beta1HTTPIngressRuleValue(
                        paths=[client.NetworkingV1beta1HTTPIngressPath(
                            path=self.path,
                            backend=client.NetworkingV1beta1IngressBackend(
                                service_port=self.target_service.port,
                                service_name=self.target_service.slug
                            )
                        )]
                    )
                )]
            )
        )

    def deploy(self):
        """
        :description: Deploy ingress to ns.
        """
        api_instance = self.get_client(API=client.ExtensionsV1beta1Api)
        body = self.get_obj()
        api_response = api_instance.create_namespaced_ingress(
            body = body,
            namespace = self.namespace
        )
        self.kuid = api_response.metadata.uid
        self.save()
        return str(api_response.status)

    def remove(self):
        """
        :description: Remove ingress from ns.
        """
        api_instance = self.get_client(API=client.ExtensionsV1beta1Api)
        api_response = api_instance.delete_namespaced_ingress(
            name = self.slug,
            namespace = self.namespace
        )
        self.kuid = None
        self.save()
        return str(api_response.status)
