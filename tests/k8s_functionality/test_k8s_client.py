import hashlib
import time
from datetime import datetime

import yaml
from kubernetes import client
from test_plus.test import TestCase

from k8s_job.models import JobInstance, TargetCluster
from k8s_job.tests.factories import JobDefinitionFactory, JobInstanceFactory, TargetClusterFactory
from k8s_job.utils import get_command_output

from ..base import BaseJobCleanupTestCase


# Create your tests here.
class K8sClientTestCase(BaseJobCleanupTestCase):
    def test_k8s_client_exists(self, job_instance=None):
        job_instance = self._get_job_instance(job_instance=job_instance)
        self.assertIsNotNone(job_instance)

    def test_k8s_client_access(self, job_instance=None):
        job_instance = self._get_job_instance(job_instance=job_instance)
        with job_instance.k8s_client as client:
            result = client.list_namespace()
            self.assertIsNotNone(result)
