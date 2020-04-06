import json
import re

from django.db import models
from django_kubernetes_manager.consts import byte_units
from kubernetes import client, config


class KubernetesTelemetryMixin(models.Model):
    """
    KubernetesTelemetryMixin
    :type: mixin
    :description: Extends child model to include telemetry features.
    :inherits: django.db.models.Model
    :fields: object_status, average_cpu_usage,
        average_mem_usage, cpu_usage_seconds, mem_usage_seconds
    """

    object_status = models.CharField(max_length=128, null=True, blank=True, help_text="status of the object in Kubernetes")
    average_cpu_usage = models.DecimalField(null=True, blank=True, max_digits=8, decimal_places=4, help_text="Average PIT CPU units consumed")
    average_mem_usage = models.IntegerField(null=True, blank=True, help_text="Average PIT bytes consumed")
    cpu_usage_seconds = models.DecimalField(null=True, blank=True, max_digits=8, decimal_places=4, help_text="Average cpu usage * seconds live")
    mem_usage_seconds = models.IntegerField(null=True, blank=True, help_text="Average mem usage * seconds live")

    class Meta:
        abstract = True

    def splitNumeric(self, size):
        """
        :description: Parses string into numeric component.
        """
        return filter(None, re.split(r"(\d+)", size))

    def parseSize(self, size):
        """
        :description: Parses string as numeric, suffix and converts to bytes.
        """
        number, unit = [string for string in self.splitNumeric(size)]
        return int(float(number) * byte_units[unit])

    def read_pod_metrics(self):
        """
        :description: Uses metrics_server to get  cadvisor data.
        """
        api_instance = self.get_client(API=client.CustomObjectsApi)
        pod_name = self.slug
        pod_namespace = self.namespace.slug
        items = api_instance.list_cluster_custom_object("metrics.k8s.io", "v1beta1", "pods").get("items", [])
        return [pod for pod in items if pod_name in pod.get("metadata", {}).get("name") and pod_namespace in pod.get("metadata", {}).get("namespace")]

    def read_pod_usage(self):
        """
        :description: Converts metrics into dictionary for api usage.
        """
        pod_name = self.pod_template.slug
        pod_namespace = self.namespace.slug
        pod_metrics = self.read_pod_metrics()
        cpu = 0.000
        memory = 0
        for metric in pod_metrics:
            for container in metric.get("containers", []):
                ccpu = container.get("usage", {}).get("cpu", None)
                cmem = container.get("usage", {}).get("memory", None)
                if "m" in ccpu:
                    ccpu = int(ccpu.split("m")[0]) / 1000.000
                else:
                    ccpu = int(ccpu)
                cpu += ccpu
                memory += self.parseSize(cmem)
        return {"cpu": cpu, "memory": memory}

    def status(self):
        """
        :description: Returns status data of object.
        """
        type = self._meta.model_name
        name = self.slug
        namespace = self.namespace.slug
        api_instance = self.get_client(API=client.ExtensionsV1beta1Api)
        if type == "kubernetesjob":
            api_response = api_instance.read_namespaced_job_status(name, namespace)
        if type == "kubernetesdeployment":
            api_response = api_instance.read_namespaced_deployment_status(name, namespace)
        return api_response.status
