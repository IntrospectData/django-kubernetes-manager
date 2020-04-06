from django_kubernetes_manager.models import (
    KubernetesBase,
    KubernetesConfigMap,
    KubernetesContainer,
    KubernetesDeployment,
    KubernetesIngress,
    KubernetesJob,
    KubernetesMetadataObjBase,
    KubernetesNamespace,
    KubernetesNetworkingBase,
    KubernetesPodTemplate,
    KubernetesService,
    KubernetesVolume,
    KubernetesVolumeMount,
    TargetCluster,
)
from rest_framework import serializers


class TargetClusterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TargetCluster
        fields = ["title", "api_endpoint", "telemetry_endpoint", "config"]


class KubernetesBaseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = KubernetesBase
        fields = ["title", "description", "cluster", "config"]
        abstract = True


class KubernetesMetadataObjBaseSerializer(KubernetesBaseSerializer):
    class Meta:
        model = KubernetesMetadataObjBase
        fields = KubernetesBaseSerializer.Meta.fields + ["labels", "annotations"]
        abstract = True


class KubernetesNetworkingBaseSerializer(KubernetesMetadataObjBaseSerializer):
    class Meta:
        model = KubernetesNetworkingBase
        fields = KubernetesMetadataObjBaseSerializer.Meta.fields + ["api_version", "kind", "port", "namespace", "kuid"]
        abstract = True


class KubernetesVolumeSerializer(KubernetesBaseSerializer):
    class Meta:
        model = KubernetesVolume
        fields = KubernetesBaseSerializer.Meta.fields


class KubernetesVolumeMountSerializer(KubernetesBaseSerializer):
    class Meta:
        model = KubernetesVolumeMount
        fields = KubernetesBaseSerializer.Meta.fields + ["mount_path", "sub_path"]


class KubernetesNamespaceSerializer(KubernetesMetadataObjBaseSerializer):
    class Meta:
        model = KubernetesNamespace
        fields = KubernetesMetadataObjBaseSerializer.Meta.fields + ["api_version", "kind", "exists"]


class KubernetesConfigMapSerializer(KubernetesMetadataObjBaseSerializer):
    class Meta:
        model = KubernetesConfigMap
        fields = KubernetesMetadataObjBaseSerializer.Meta.fields + [
            "data",
            "kind",
        ]


class KubernetesContainerSerializer(KubernetesBaseSerializer):
    class Meta:
        model = KubernetesContainer
        fields = KubernetesBaseSerializer.Meta.fields + ["image_name", "image_tag", "image_pull_policy", "command", "args", "port", "volume_mount"]


class KubernetesPodTemplateSerializer(KubernetesMetadataObjBaseSerializer):
    class Meta:
        model = KubernetesPodTemplate
        fields = KubernetesMetadataObjBaseSerializer.Meta.fields + ["volume", "primary_container", "secondary_container", "restart_policy"]


class KubernetesDeploymentSerializer(KubernetesNetworkingBaseSerializer):
    class Meta:
        model = KubernetesDeployment
        fields = KubernetesNetworkingBaseSerializer.Meta.fields + ["selector", "replicas", "pod_template"]


class KubernetesJobSerializer(KubernetesNetworkingBaseSerializer):
    class Meta:
        model = KubernetesJob
        fields = KubernetesNetworkingBaseSerializer.Meta.fields + ["backoff_limit", "pod_template"]


class KubernetesServiceSerializer(KubernetesNetworkingBaseSerializer):
    class Meta:
        model = KubernetesService
        fields = KubernetesNetworkingBaseSerializer.Meta.fields + ["selector", "target_port"]


class KubernetesIngressSerializer(KubernetesNetworkingBaseSerializer):
    class Meta:
        model = KubernetesIngress
        fields = KubernetesNetworkingBaseSerializer.Meta.fields + ["hostname", "path", "target_service"]
