import json
from time import sleep

from django.contrib.postgres.fields import JSONField
from django.db import models
from kubernetes_manager.consts import PULL_POLICY, RESTART_POLICY
from kubernetes import client, config

from .base import KubernetesBase, KubernetesMetadataObjBase, KubernetesNetworkingBase
from .mixins import KubernetesTelemetryMixin


class KubernetesNamespace(KubernetesMetadataObjBase):
    """
    KubernetesNamespace
    :type: model
    :description: Holds data related to a Kubernetes namespace.
    :inherits: kubernetes_manager.models.base.KubernetesBase
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
            api_version=self.api_version,
            kind=self.kind,
            metadata=client.V1ObjectMeta(name=self.slug, labels=self.labels, annotations=self.annotations),
            spec=client.V1NamespaceSpec(),
        )

    def deploy(self):
        """
        :description: Deploy namespace obj.
        """
        api_instance = self.get_client(API=client.CoreV1Api)
        body = self.get_obj()
        api_response = api_instance.create_namespace(body=body,)
        self.exists = True
        self.save()
        return str(api_response.status)

    def remove(self):
        """
        :description: Delete namespace from cluster.
        """
        api_instance = self.get_client(API=client.CoreV1Api)
        api_response = api_instance.delete_namespace(name=self.slug,)
        self.exists = False
        self.save()
        return str(api_response.status)


class KubernetesVolume(KubernetesBase):
    """
    KubernetesVolume
    :type: model
    :description: Holds data related to a kubernetes volume.
    :inherits: kubernetes_manager.models.base.KubernetesBase
    :fields: *
    """

    def get_obj(self):
        """
        :description: Generate volume spec.
        """
        if self.config.get("configmap"):
            return client.V1Volume(name=self.slug, config_map=client.V1ConfigMapVolumeSource(name=self.config.get("configmap")))
        return client.V1Volume(name=self.slug, empty_dir=client.V1EmptyDirVolumeSource())


class KubernetesVolumeMount(KubernetesBase):
    """
    KubernetesVolumeMount
    :type: model
    :description: Holds data related to a kubernetes volume mount.
    :inherits: kubernetes_manager.models.base.KubernetesBase
    :fields: mount_path, sub_path
    """

    mount_path = models.CharField(max_length=255, default="/media")
    sub_path = models.CharField(max_length=255, default=None, null=True, blank=True)

    def get_obj(self):
        """
        :description: Generate mount spec.
        """
        return client.V1VolumeMount(name=self.slug, mount_path=self.mount_path, sub_path=self.sub_path)


class KubernetesContainer(KubernetesBase):
    """
    KubernetesContainer
    :type: model
    :description: Holds data related to a kubernetes contaienr.
    :inherits: kubernetes_manager.models.base.KubernetesBase
    :fields: image_name, image_tag, image_pull_policy, command, args, port,
        volume_mount
    """

    image_name = models.CharField(max_length=200, db_index=True, help_text="Properly qualified image name.", default="debian")
    image_tag = models.CharField(max_length=100, db_index=True, help_text="Tag name for the image to be used for this job", default="latest")
    image_pull_policy = models.CharField(max_length=16, choices=PULL_POLICY, default="IfNotPresent")
    command = models.TextField(help_text="Command to run when start container", null=True, blank=True)
    args = models.TextField(
        help_text="Comma separated args to run with command\
        when instantiating container.",
        null=True,
        blank=True,
    )
    port = models.IntegerField(default=80, help_text="Port to expose.")
    volume_mounts = models.ManyToManyField("KubernetesVolumeMount", blank=True, help_text="Mounts for any number of volumes")

    def get_obj(self):
        """
        :description: Generate container spec.
        """
        return client.V1Container(
            name=self.slug,
            image=":".join([self.image_name, self.image_tag]),
            image_pull_policy=self.image_pull_policy,
            ports=[client.V1ContainerPort(container_port=self.port)],
            volume_mounts=[
                vm.get_obj() for vm in self.volume_mounts.all()
            ] if self.volume_mounts else None,
            command=[self.command] if self.command else None,
            args=self.args.split(",") if self.args else None,
        )


class KubernetesConfigMap(KubernetesMetadataObjBase):
    """
    KubernetesConfigMap
    :type: model
    :description: Holds data related to a kubernetes volume mount.
    :inherits: kubernetes_manager.models.base.KubernetesMetadataObjBase
    :fields: kind, data, binary, override_name, namespace
    """

    kind = models.CharField(max_length=16, default="ConfigMap")
    data = JSONField(default=dict, null=True, blank=True)
    binary = models.BinaryField(null=True, blank=True)
    override_name = models.CharField(max_length=32, null=True, blank=True, default="ConfigMap")
    namespace = models.ForeignKey("KubernetesNamespace", on_delete=models.CASCADE)

    def get_obj(self):
        """
        :description: Generate configmap spec.
        """
        return client.V1ConfigMap(
            metadata=client.V1ObjectMeta(name=self.slug, labels=self.labels, annotations=self.annotations),
            kind=self.kind,
            data=self.data if self.data else None,
            binary_data={str(self.override_name): self.binary} if self.binary else None,
        )

    def deploy(self):
        """
        :description: Deploy configmap obj.
        """
        api_instance = self.get_client(API=client.CoreV1Api)
        body = self.get_obj()
        api_response = api_instance.create_namespaced_config_map(body=body, namespace=self.namespace.slug)
        self.kuid = api_response.metadata.uid
        self.save()
        return str(api_response.status)

    def remove(self):
        """
        :description: Delete configmap from namespace.
        """
        api_instance = self.get_client(API=client.CoreV1Api)
        api_response = api_instance.delete_namespaced_config_map(name=self.slug, namespace=self.namespace.slug)
        self.kuid = None
        self.save()
        return str(api_response.status)


class KubernetesPodTemplate(KubernetesMetadataObjBase):
    """
    KubernetesPodTemplate
    :type: model
    :description: Holds data related to a kubernetes pod spec.
    :inherits: kubernetes_manager.models.base.KubernetesMetadataObjBase
    :fields: volume, primary_container, secondary_container, restart_policy
    """

    volumes = models.ManyToManyField("KubernetesVolume", blank=True, help_text="All volumes to be created for a pod.")
    containers = models.ManyToManyField("KubernetesContainer", help_text="All containers to be included in a pod.")
    restart_policy = models.CharField(max_length=16, choices=RESTART_POLICY, default="Never", help_text="How the pod should handle restart om case of failures")

    def get_obj(self):
        """
        :description: Generate pod spec.
        """
        if self.containers:
            return client.V1PodTemplateSpec(
                metadata=client.V1ObjectMeta(name=self.slug, labels=self.labels, annotations=self.annotations),
                spec=client.V1PodSpec(
                    volumes=[
                        v.get_obj() for v in self.volumes.all()
                     ] if self.volumes is not None else None,
                    containers=[
                        c.get_obj() for c in self.containers.all()
                    ],
                    restart_policy=self.restart_policy,
                ),
            )
        else:
            raise ValueError("Containers cannot be empty or null")


class KubernetesDeployment(KubernetesNetworkingBase, KubernetesTelemetryMixin):
    """
    KubernetesDeployment
    :type: model
    :description: Holds data related to a kubernetes deployment.
    :inherits: kubernetes_manager.models.base.KubernetesNetworkingBase,
        kubernetes_manager.models.base.KubernetesTelemetryMixin
    :fields: selector, replicas, pod_template
    """

    selector = JSONField(default=dict)
    replicas = models.IntegerField(default=1)
    pod_template = models.ForeignKey("KubernetesPodTemplate", on_delete=models.CASCADE)

    def get_obj(self):
        """
        :description: Generate Deployment spec.
        """
        return client.V1Deployment(
            api_version=self.api_version,
            kind=self.kind,
            metadata=client.V1ObjectMeta(name=self.slug, labels=self.labels, annotations=self.annotations),
            spec=client.V1DeploymentSpec(selector=client.V1LabelSelector(match_labels=self.selector), replicas=self.replicas, template=self.pod_template.get_obj()),
        )

    def deploy(self):
        """
        :description: Deploy deployment obj.
        """
        api_instance = self.get_client(API=client.AppsV1Api)
        body = self.get_obj()
        api_response = api_instance.create_namespaced_deployment(body=body, namespace=self.namespace.slug)
        ticker = 0
        while self.status().unavailable_replicas > 0:
            if ticker >= self.config.get("timeout", 60):
                raise Exception("Timeout: no replicas available after {} ticks".format(str(ticker)))
            ticker += 1
            sleep(1)
        self.kuid = api_response.metadata.uid
        self.save()
        return str(api_response.status)

    def remove(self):
        """
        :description: Remove deployment from namespace.
        """
        api_instance = self.get_client(API=client.AppsV1Api)
        api_response = api_instance.delete_namespaced_deployment(name=self.slug, namespace=self.namespace.slug)
        self.kuid = None
        self.save()
        return str(api_response.status)


class KubernetesJob(KubernetesNetworkingBase, KubernetesTelemetryMixin):
    """
    KubernetesJob
    :type: model
    :description: Holds data related to a kubernetes pod spec.
    :inherits: kubernetes_manager.models.base.KubernetesNetworkingBase,
        kubernetes_manager.models.base.KubernetesTelemetryMixin
    :fields: selector, replicas, pod_template
    """

    pod_template = models.ForeignKey("KubernetesPodTemplate", on_delete=models.CASCADE)
    backoff_limit = models.IntegerField(default=3)

    def get_obj(self):
        """
        :description: Generate job spec.
        """
        return client.V1Job(
            api_version=self.api_version,
            kind=self.kind,
            metadata=client.V1ObjectMeta(name=self.slug, labels=self.labels, annotations=self.annotations),
            spec=client.V1JobSpec(template=self.pod_template.get_obj(), backoff_limit=self.backoff_limit, ttl_seconds_after_finished=10),
        )

    def deploy(self):
        """
        :description: Deploy job to ns.
        """
        api_instance = self.get_client(API=client.BatchV1Api)
        body = self.get_obj()
        api_response = api_instance.create_namespaced_job(body=body, namespace=self.namespace.slug)
        self.kuid = api_response.metadata.uid
        self.save()
        return str(api_response.status)

    def remove(self):
        """
        :description: Remove job from ns.
        """
        api_instance = self.get_client(API=client.BatchV1Api)
        api_response = api_instance.delete_namespaced_job(name=self.slug, namespace=self.namespace.slug)
        self.kuid = None
        self.save()
        return str(api_response.status)


class KubernetesService(KubernetesNetworkingBase):
    """
    KubernetesService
    :type: model
    :description: Holds data related to a kubernetes service.
    :inherits: kubernetes_manager.models.base.KubernetesNetworkingBase
    :fields: selector, target_port
    """

    selector = JSONField(default=dict)
    target_port = models.IntegerField(default=80)

    def get_obj(self):
        """
        :description: Generate service spec.
        """
        return client.V1Service(
            api_version=self.api_version,
            kind=self.kind,
            metadata=client.V1ObjectMeta(name=self.slug, labels=self.labels, annotations=self.annotations),
            spec=client.V1ServiceSpec(
                selector=client.V1LabelSelector(match_labels=self.selector), ports=[client.V1ServicePort(port=self.port, target_port=self.target_port)]
            ),
        )

    def deploy(self):
        """
        :description: Deploy service to ns.
        """
        api_instance = self.get_client(API=client.ExtensionsV1beta1Api)
        body = self.get_obj()
        api_response = api_instance.create_namespaced_service(body=body, namespace=self.namespace.slug)
        self.kuid = api_response.metadata.uid
        self.save()
        return str(api_response.status)

    def remove(self):
        """
        :description: Remove service from ns.
        """
        api_instance = self.get_client(API=client.ExtensionsV1beta1Api)
        api_response = api_instance.delete_namespaced_service(name=self.slug, namespace=self.namespace.slug)
        self.kuid = None
        self.save()
        return str(api_response.status)


class KubernetesIngress(KubernetesNetworkingBase):
    """
    KubernetesIngress
    :type: model
    :description: Holds data related to a kubernetes ingress.
    :inherits: kubernetes_manager.models.base.KubernetesNetworkingBase
    :fields: hostname, path, target_service
    """

    hostname = models.CharField(max_length=255, default="localhost")
    path = models.CharField(max_length=255, default="/")
    target_service = models.ForeignKey("KubernetesService", on_delete=models.CASCADE)

    def get_obj(self):
        """
        :description: Generate ingress obj.
        """
        return client.NetworkingV1beta1Ingress(
            api_version=self.api_version,
            kind=self.kind,
            metadata=client.V1ObjectMeta(name=self.slug, annotations=self.annotations),
            spec=client.NetworkingV1beta1IngressSpec(
                selector=client.V1LabelSelector(match_labels=self.selector),
                rules=[
                    client.NetworkingV1beta1IngressRule(
                        host=self.hostname,
                        http=client.NetworkingV1beta1HTTPIngressRuleValue(
                            paths=[
                                client.NetworkingV1beta1HTTPIngressPath(
                                    path=self.path,
                                    backend=client.NetworkingV1beta1IngressBackend(service_port=self.target_service.port, service_name=self.target_service.slug),
                                )
                            ]
                        ),
                    )
                ],
            ),
        )

    def deploy(self):
        """
        :description: Deploy ingress to ns.
        """
        api_instance = self.get_client(API=client.ExtensionsV1beta1Api)
        body = self.get_obj()
        api_response = api_instance.create_namespaced_ingress(body=body, namespace=self.namespace.slug)
        self.kuid = api_response.metadata.uid
        self.save()
        return str(api_response.status)

    def remove(self):
        """
        :description: Remove ingress from ns.
        """
        api_instance = self.get_client(API=client.ExtensionsV1beta1Api)
        api_response = api_instance.delete_namespaced_ingress(name=self.slug, namespace=self.namespace.slug)
        self.kuid = None
        self.save()
        return str(api_response.status)
