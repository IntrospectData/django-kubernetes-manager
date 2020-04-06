from django.contrib import admin
from django_kubernetes_manager.models import (
    KubernetesConfigMap,
    KubernetesContainer,
    KubernetesDeployment,
    KubernetesIngress,
    KubernetesJob,
    KubernetesNamespace,
    KubernetesPodTemplate,
    KubernetesService,
    KubernetesVolume,
    KubernetesVolumeMount,
    TargetCluster,
)

models = [
    TargetCluster,
    KubernetesContainer,
    KubernetesPodTemplate,
    KubernetesJob,
    KubernetesDeployment,
    KubernetesService,
    KubernetesIngress,
    KubernetesNamespace,
    KubernetesConfigMap,
    KubernetesVolume,
    KubernetesVolumeMount,
]

for model in models:
    admin.site.register(model)
