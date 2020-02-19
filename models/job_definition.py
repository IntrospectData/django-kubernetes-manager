from uuid import uuid4

from core.common.models import UUIDAuditModelBase
from core.db.fields import EncryptedJSONField
from django.contrib.postgres.fields import JSONField
from django.db import models
from django_extensions.db.models import TimeStampedModel, TitleSlugDescriptionModel
from k8s_job.utils import log


# Create your models here.
class JobDefinition(TitleSlugDescriptionModel, UUIDAuditModelBase):
    """Reusable Kubernetes Job definition which holds logic for creating properly formatted k8s object(s)"""

    lineage_id = models.UUIDField(default=uuid4, editable=False, db_index=True, help_text="Lineage ID which links all jobs that descend from the same root")
    parent = models.ForeignKey(
        "self", db_index=True, null=True, blank=True, on_delete=models.CASCADE, related_name="child_items", help_text="Parent JobDefinition this JobDefinition was created from"
    )
    image_name = models.CharField(max_length=200, db_index=True, help_text="Properly qualified image name to execute this job within")
    image_tag = models.CharField(max_length=100, db_index=True, help_text="Tag name for the image to be used for this job", default="latest")
    command = models.TextField(help_text="Command to run when instantiating this job definition", null=True, blank=True)
    script = models.TextField(help_text="Script to run when instantiating this job definition", null=True, blank=True)
    cluster = models.ForeignKey(
        "TargetCluster",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="job_definitions",
        help_text="Optional TargetCluster to specify as the intended target of this JobDefinition",
    )
    config = EncryptedJSONField(help_text="Configuration data stored as an encrypted blob in the database")

    def get_image(self):
        """Get image identifier based on image name/tag"""
        return "{}:{}".format(self.image_name, self.image_tag)

    image = property(get_image)

    def save(self, *args, **kwargs):
        """Save override for JobDefinition to force a new object to be created vs. updating existing for history and consistency for audit/reporting"""
        if self.id and not self._state.adding:
            log.debug("Saving lineage id {} by setting old id {} to None".format(self.lineage_id, self.id))
            self.id = None
        super().save(*args, **kwargs)

    class Meta(UUIDAuditModelBase.Meta):
        verbose_name = "Job Definition"
        verbose_name_plural = "Job Definitions"
