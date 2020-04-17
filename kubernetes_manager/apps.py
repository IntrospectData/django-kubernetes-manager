from django.apps import AppConfig


class KubernetesManagerConfig(AppConfig):
    name = "kubernetes_manager"
    verbose_name = "Kubernetes Manager"

    def ready(self):
        pass
