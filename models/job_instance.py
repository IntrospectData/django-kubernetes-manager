import contextlib
import json
import time
from datetime import datetime
from tempfile import NamedTemporaryFile
from uuid import uuid4

import dateparser
from core.common.models import UUIDAuditModelBase
from core.db.fields import EncryptedJSONField
from django.contrib.postgres.fields import JSONField
from django.db import models
from django.utils import timezone
from django_extensions.db.models import TimeStampedModel
from kubernetes import client
from kubernetes.client.rest import ApiException
from kubernetes.config import new_client_from_config

from ..utils import find_namespaced_pods, log, create_job_obj, run_job, delete_job
from .log_entry import LogEntry
from .obj.k8s_config_map import K8sConfigMap
from .obj.k8s_job import K8sJob
from .telemetry_entry import TelemetryEntry


# Create your models here.
class JobInstance(UUIDAuditModelBase):
    """Instance of a given job that has been requested to execute within a given cluster."""

    notes = models.TextField(null=True, blank=True, help_text="User-specified notes for reference purposes later")
    job_definition = models.ForeignKey(
        "JobDefinition",
        db_index=True,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="instances",
        help_text="JobDefinition that this JobInstance was created from",
    )
    env_vars = EncryptedJSONField(default=dict, help_text="Key/Value pair representing environment variables to assign to this JobInstance")
    script = models.TextField(null=True, help_text="Optional override to specify a script for this instance of a K8s Job", blank=True)
    namespace = models.CharField(max_length=50, help_text="Namespace this job will be executed within", default="default")
    timestamps = JSONField(default=dict, help_text="Control flow timestamps.", blank=True)
    cluster = models.ForeignKey(
        "TargetCluster", on_delete=models.CASCADE, related_name="job_instances", help_text="Cluster to use when operating on this k8s cluster for this job instance"
    )
    config = EncryptedJSONField(help_text="Configuration data stored as an encrypted blob in the database")
    vcpu_seconds = models.DecimalField(null=True, max_digits=64, decimal_places=8, help_text="Moving average of cores * seconds in pod lifecycle.")
    byte_seconds = models.DecimalField(null=True, max_digits=64, decimal_places=8, help_text="Moving average of bytes * seconds in pod lifecycle.")

    class Meta(UUIDAuditModelBase.Meta):
        verbose_name = "Job Instance"
        verbose_name_plural = "Job Instances"

    def save(self, *args, **kwargs):
        for k in self.timestamps.keys():
            if isinstance(self.timestamps[k], datetime):
                self.timestamps[k] = self.timestamps[k].isoformat()
        super().save(*args, **kwargs)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for k in self.timestamps.keys():
            if isinstance(self.timestamps[k], str):
                self.timestamps[k] = dateparser.parse(self.timestamps[k])

    @classmethod
    def add_log(cls, job_instance, message, parse_timestamp=False, **kwargs):
        return LogEntry.add(job_instance=job_instance, message=message, parse_timestamp=parse_timestamp, **kwargs)

    def add_log(self, message, parse_timestamp=False, **kwargs):
        return LogEntry.add(job_instance=self, message=message, parse_timestamp=parse_timestamp, **kwargs)

    @classmethod
    def add_metric(cls, job_instance, data, **kwargs):
        return TelemetryEntry.add(job_instance=job_instance, data=data, **kwargs)

    def add_metric(self, data, **kwargs):
        return TelemetryEntry.add(job_instance=self, data=data, **kwargs)

    @contextlib.contextmanager
    def get_k8s_client(self, API=client.CoreV1Api, **kwargs):
        """Gets a k8s api client based on the credential associated with this JobInstance

            Args:
                API (client.<type>) - Kubernetes Client Type
            Returns:
                object of type <API>
        """
        if "persist_config" not in kwargs:
            kwargs["persist_config"] = False
        with NamedTemporaryFile() as ntf:
            kwargs["config_file"] = ntf.name
            if isinstance(self.cluster.config, dict):
                cc = json.dumps(self.cluster.config)
            else:
                cc = self.cluster.config
            with open(ntf.name, "w") as f:
                f.write(cc)
            yield API(api_client=new_client_from_config(**kwargs))

    k8s_client = property(get_k8s_client)

    def schedule(self):
        """Schedules this set of resources on the target k8s cluster"""
        if not self.timestamps.get("scheduled"):
            self.timestamps["scheduled"] = timezone.now()
        self.save()

    def create(self):
        """Creates the configmap and job on the target k8s cluster"""
        if self.job.create():
            self.timestamps["created"] = timezone.now()
            run_job(
                create_job_obj(),

            )
            return True
        return False

    def delete(self):
        """Deletes this set of resources on the target k8s cluster"""
        self.job.delete()
        self.config_map.delete()
        if not self.timestamps.get("deleted"):
            self.timestamps["deleted"] = timezone.now()

    def get_is_complete(self):
        return True if len(set(["succeeded", "failed", "cleanup"]).intersection(self.timestamps.keys())) > 0 else False

    is_complete = property(get_is_complete)

    def get_is_successful(self):
        return True if self.timestamps.get("succeeded") else False

    is_successful = property(get_is_successful)

    def get_is_failed(self):
        return True if self.timestamps.get("failed") else False

    is_failed = property(get_is_failed)

    def poll_status(self, update=True):
        """Checks the status of the kubernetes job created by this object"""
        ret_val = None
        if not self.is_complete:
            status = self.job.read().status
            if status.get("active", -1) > 0:
                if update and not self.timestamps.get("active"):
                    self.timestamps["active"] = status.get("start_time", timezone.now())
                ret_val = "active"
            elif status.get("succeeded", -1) > 0:
                if update and not self.timestamps.get("success"):
                    self.timestamps["success"] = status.get("completion_time", timezone.now())
                ret_val = "succeeded"
            elif status.get("failed", -1) > 0:
                if update and not self.timestamps.get("failed"):
                    self.timestamps["failed"] = status.get("completion_time", timezone.now())
                ret_val = "failed"
            if ret_val:
                self.save()
        return ret_val

    def get_config_map(self):
        """Helper method to hydrate K8sConfigMap object with job instance data"""
        return K8sConfigMap(job_instance=self)

    config_map = property(get_config_map)

    def get_job(self):
        """Helper method to hydrate K8sJob object with job instance data"""
        return K8sJob(job_instance=self)

    job = property(get_job)

    def cleanup(self):
        """Removes all k8s resources associted with this JobInstance"""
        deletes = []
        ret_val = False
        if self.config_map.read():
            deletes.append(self.config_map.delete())
            log.debug("Called to delete ConfigMap for {}".format(self.id))
        if self.job.read():
            deletes.append(self.job.delete())
            log.debug("Called to delete Job for {}".format(self.id))
        if any(deletes):
            self.timestamps["cleanup"] = timezone.now()
            self.save()
            ret_val = True
        return ret_val
