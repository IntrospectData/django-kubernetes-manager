import json
from uuid import uuid4

from core.common.models import DataEntryBase
from django.contrib.postgres.fields import JSONField
from django.db import models
from django.utils import timezone
from k8s_job.utils import log

from ..utils import get_dict_hash

METRIC_KEYS = [
    "container_memory_usage_bytes",
    "container_cpu_usage_seconds_total",
    "container_network_receive_bytes_total",
    "container_network_transmit_bytes_total",
    "container_fs_writes_bytes_total",
    "container_fs_reads_bytes_total",
    "container_last_seen",
]
# Create your models here.
class TelemetryEntry(DataEntryBase):
    """Metric data pertaining to a given job instance"""

    data_hash = models.CharField(db_index=True, max_length=32, editable=False, help_text="Hash of the json data after it has been ordered in a consistent manner")
    data = JSONField(default=dict, help_text="JSON-serialized dictionary holding the data for a specific point in time and a given JobInstance")
    job_instance = models.ForeignKey(
        "JobInstance", db_index=True, null=True, blank=True, on_delete=models.CASCADE, related_name="telemetry", help_text="JobInstance that this data is related to"
    )
    created = models.DateTimeField(auto_now_add=True)
    def save(self, *args, **kwargs):
        """Additional save logic to handle persisting the data hash if it's not provided"""
        if not self.data_hash:
            self.data_hash = get_dict_hash(self.data)
        super().save(*args, **kwargs)

    class Meta(DataEntryBase.Meta):
        verbose_name = "Telemetry Data Point"
        verbose_name_plural = "Telemetry Data"
        unique_together = DataEntryBase.Meta.unique_together + [["job_instance", "data_hash", "created"]]
        index_together = DataEntryBase.Meta.index_together + [["job_instance", "data_hash"]]

    @classmethod
    def add(cls, job_instance, data={}, **kwargs):
        """Helper class method to create a new metric that handles deduplication based on the hash of the data object

            Args:
                job_instance (JobInstance) - JobInstance that the metric data is related to
                data (dict) - dictionary of metric data
                as_of (TZ-aware DateTime) - Timestamp
            Returns;
                boolean - True if created, False if not
        """
        if "as_of" not in kwargs:
            kwargs["as_of"] = timezone.now()
        kwargs["data_hash"] = get_dict_hash(data)
        kwargs["data"] = data
        kwargs["job_instance"] = job_instance
        ret_val = None
        create = False
        q = cls.objects.filter(job_instance=job_instance).order_by("-as_of")
        if q.count() > 0:
            metric = q.first()
            log.debug("Previous metric {} has hash of {}".format(metric.id, metric.data_hash))
            log.debug("New data hash is {}".format(kwargs["data_hash"]))
            if getattr(metric, "data_hash", None) != kwargs["data_hash"]:
                create = True
            else:
                ret_val = None
        else:
            create = True
        if create:
            ret_val = cls(**kwargs)
            ret_val.save()
        return ret_val
