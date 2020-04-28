import json
from tempfile import NamedTemporaryFile
from uuid import uuid4

from django.contrib.postgres.fields import JSONField
from django.db import models
from django_extensions.db.models import TitleSlugDescriptionModel
from kubernetes import client, config


class KubernetesBase(models.Model):
    """
    KubernetesBase
    :type: model (abstract)
    :description: Base parent model that all subsequent models inherit from.
    :inherits: django_extensions.db.models.TitleSlugDescriptionModel
    :fields: id, cluster, config, deployed, deleted
    """

    id = models.UUIDField(default=uuid4, editable=False, primary_key=True, help_text="UUID Auto field.")
    title = models.CharField(max_length=128)
    cluster = models.ForeignKey("TargetCluster", on_delete=models.SET_NULL, null=True, help_text="ForeignKey to TargetCluster object.")
    config = JSONField(default=dict, null=True, blank=True, help_text="Pass in extra parameters here.")
    deployed = models.DateTimeField(null=True, blank=True, help_text="Time when object is applied to cluster.")
    removed = models.DateTimeField(null=True, blank=True, help_text="Time when object is removed from cluster.")

    class Meta:
        abstract = True

    def slugify_function(self):
        """
        :description: Overrides default slugify with custom logic.
        """
        return self.title.replace("_", "-").replace(" ", "-").lower()
    
    @property
    def slug(self):
        return self.slugify_function()

    def get_client(self, API=client.CoreV1Api, **kwargs):
        """Gets a k8s api client

            Args:
                API (client.<type>) - Kubernetes Client Type
            Returns:
                object of type <API>
        """

        if "persist_config" not in kwargs:
            kwargs["persist_config"] = False
        with NamedTemporaryFile() as ntf:
            kwargs["config_file"] = ntf.name
            cc = json.dumps(self.cluster.config) if isinstance(self.cluster.config, dict) else self.cluster.config
            with open(ntf.name, "w") as f:
                f.write(cc)
            return API(api_client=config.new_client_from_config(config_file=ntf.name))


class KubernetesMetadataObjBase(KubernetesBase):
    """
    KubernetesMetadataObjBase
    :type: model (abstract)
    :description: Extends KubernetesBase to include metadata fields.
    :inherits: kubernetes_manager.models.base.KubernetesBase
    :fields: labels, annotations
    """

    labels = JSONField(default=dict, help_text="Dictionary store equivalent to Labels in Kubernetes API")
    annotations = JSONField(default=dict, null=True, blank=True, help_text="Dictionary store equivalent to Annotations in Kubernetes API")

    class Meta:
        abstract = True


class KubernetesNetworkingBase(KubernetesMetadataObjBase):
    """
    KubernetesNetworkingBase
    :type: model (abstract)
    :description: Extends KubernetesMetadataObjBase to include network fields.
    :inherits: kubernetes_manager.models.base.KubernetesMetadataObjBase
    :fields: labels, annotations
    """

    api_version = models.CharField(max_length=16, default="v1", help_text="API version used to deploy child object.")
    kind = models.CharField(max_length=16, help_text="String representation of Kubernetes object kind")
    port = models.IntegerField(default=80, help_text="Port object will expose")
    namespace = models.ForeignKey("KubernetesNamespace", on_delete=models.CASCADE, help_text="Live namespace the object is associated with.")
    kuid = models.CharField(max_length=48, null=True, blank=True, help_text="Object's UID in the cluster")

    class Meta:
        abstract = True
