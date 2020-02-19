import json

from kubernetes import client
from kubernetes.client.rest import ApiException
from django.db import models
from .target_cluster import TargetCluster

class KubernetesBase(model.Model):
    id = models.UUIDField(default=uuid4, editable=False)
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=128)
    namespace = models.CharField(max_length=128)
    cluster = models.ForeignKey(TargetCluster)
