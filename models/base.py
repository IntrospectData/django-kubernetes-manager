import json

from kubernetes import client
from kubernetes.client.rest import ApiException
from django.db import models

class KubernetesBase(model.Model):
    id
    name
    description
    namespace
    cluster
    
