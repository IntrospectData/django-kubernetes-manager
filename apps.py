from core.common.apps import AbstractAppConfig


class K8SJobConfig(AbstractAppConfig):
    name = "k8s_job"
    verbose_name = "ID - K8s Jobs"

    def ready(self):
        super().ready(["JobDefinition", "JobInstance", "LogEntry", "TargetCluster", "TelemetryEntry"])
