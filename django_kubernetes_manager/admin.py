from django.contrib import admin
from django_kubernetes_manager.models import (TargetCluster,
    KubernetesContainer, KubernetesPodTemplate, KubernetesJob,
    KubernetesDeployment, KubernetesService, KubernetesIngress,
    KubernetesNamespace)

models = [TargetCluster,
    KubernetesContainer, KubernetesPodTemplate, KubernetesJob,
    KubernetesDeployment, KubernetesService, KubernetesIngress,
    KubernetesNamespace]

for model in models:
    admin.site.register(model)
