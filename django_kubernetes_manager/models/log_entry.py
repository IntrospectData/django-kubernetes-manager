import json
from uuid import uuid4

from django.db import models
from django.utils import timezone

import dateparser
from core.common.models import DataEntryBase

from ..utils import log

LOG_ENTRY_SOURCE = [("p", "Pod Logs"), ("k", "Kubernetes Events"), ("e", "Other Errors")]
# Create your models here.
class LogEntry(DataEntryBase):
    """Log entry pertaining to a given job instance"""

    message = models.TextField(db_index=True, help_text="Log entry text")
    job_instance = models.ForeignKey(
        "JobInstance", db_index=True, null=True, blank=True, on_delete=models.CASCADE, related_name="logs", help_text="JobInstance that this data is related to"
    )
    pod_id = models.CharField(max_length=128, null=True, blank=True)
    source = models.CharField(max_length=1, choices=LOG_ENTRY_SOURCE, default="p")

    def save(self, *args, **kwargs):
        if not self.as_of:
            self.as_of = self.created
        super().save(*args, **kwargs)

    class Meta(DataEntryBase.Meta):
        verbose_name = "Log Entry"
        verbose_name_plural = "Log Entries"
        unique_together = DataEntryBase.Meta.unique_together + [["job_instance", "message", "as_of"]]
        # index_together = [["instance", "data_hash"]]

    @classmethod
    def add(cls, job_instance, message, parse_timestamp=True, **kwargs):
        """Class-level helper for adding a new LogEntry

            Args:
                job_instance (JobInstance) -
                message (str) -
                parse_timestamp (bool) - (default: True)
            Returns:
                LogEntry
        """
        ret_val = False
        kwargs["job_instance"] = job_instance
        if "source" not in kwargs:
            kwargs["source"] = "p"
        if message.strip() and len(message.strip().split(" ")) > 1 and parse_timestamp:
            ts_str, entry = message.split(" ", 1)
            kwargs["as_of"] = dateparser.parse(ts_str)
            kwargs["message"] = entry.strip()
        elif message.strip():
            kwargs["message"] = message.strip()
        if "as_of" not in kwargs:
            kwargs["as_of"] = timezone.now()
        if "message" in kwargs:
            entry, ret_val = cls.objects.get_or_create(**kwargs)
            if ret_val:
                log.debug("Created new log entry for {} - {} - {}".format(job_instance.id, kwargs["as_of"].isoformat(), message))
        return ret_val
