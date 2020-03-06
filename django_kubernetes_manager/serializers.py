from models import (KubernetesBase, KubernetesContainer, KubernetesDeployment,
                    KubernetesIngress, KubernetesJob,
                    KubernetesMetadataObjBase, KubernetesNetworkingBase,
                    KubernetesPodTemplate, KubernetesService)
from rest_framework import serializers


class KubernetesBaseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = KubernetesBase
        fields = ['name', 'description', 'cluster', 'config']
        abstract = True



class KubernetesContainerSerializer(KubernetesBaseSerializer):
    class Meta:
        model = KubernetesContainer
        fields = [
            field for field in KubernetesBaseSerializer.Meta.fields,
            'image_name', 'image_tag', 'image_pull_policy',
            'command', 'args', 'port', 'volume'
        ]



class KubernetesMetadataObjBaseSerializer(KubernetesBaseSerializer):
    class Meta:
        model = KubernetesMetadataObjBase
        fields = [
            field for field in KubernetesBaseSerializer.Meta.fields,
            'labels', 'annotations'
        ]
        abstract = True



class KubernetesPodTemplateSerializer(KubernetesMetadataObjBaseSerializer):
    class Meta:
        model = KubernetesPodTemplate
        fields = [
            field for field in KubernetesMetadataObjBaseSerializer.Meta.fields,
            'volume', 'primary_container', 'secondary_container',
            'restart_policy'
        ]



class KubernetesNetworkingBaseSerializer(KubernetesMetadataObjBaseSerializer):
    class Meta:
        model = KubernetesNetworkingBase
        fields = [
            field for field in KubernetesMetadataObjBaseSerializer.Meta.fields,
            'api_version', 'kind', 'port', 'namespace', 'kuid'
        ]
        abstract = True



class KubernetesDeploymentSerializer(KubernetesNetworkingBaseSerializer):
    class Meta:
        model = KubernetesDeployment
        fields = [
            field for field in KubernetesNetworkingBaseSerializer.Meta.fields,
            'selector', 'replicas', 'pod_template'
        ]



class KubernetesJobSerializer(KubernetesNetworkingBaseSerializer):
    class Meta:
        model = KubernetesJob
        fields = [
            field for field in KubernetesNetworkingBaseSerializer.Meta.fields,
            'backoff_limit', 'pod_template'
        ]



class KubernetesServiceSerializer(KubernetesNetworkingBaseSerializer):
    class Meta:
        model = KubernetesService
        fields = [
            field for field in KubernetesNetworkingBaseSerializer.Meta.fields,
            'selector', 'target_port'
        ]



class KubernetesIngressSerializer(KubernetesNetworkingBaseSerializer):
    class Meta:
        model = KubernetesIngress
        fields = [
            field for field in KubernetesNetworkingBaseSerializer.Meta.fields,
            'hostname', 'path', 'target_service'
        ]
