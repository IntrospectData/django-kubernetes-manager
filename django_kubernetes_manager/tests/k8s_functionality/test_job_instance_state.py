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
class JobInstanceCleanupTestCase(BaseJobCleanupTestCase):
    # fixtures = []

    def test_new_to_initialized(self):
        job_instance = self._get_job_instance()
        job_instance.save()
        job_instance.schedule()
        self.assertTrue(job_instance.timestamps.get("scheduled"))

    def test_new_to_started(self):
        job_instance = self._get_job_instance()
        job_instance.create()
        self.assertIsNotNone(job_instance.timestamps.get("created"))
        return job_instance

    def test_deleted(self):
        job_instance = self.test_new_to_started()
        job_instance.delete()
        self.assertIsNotNone(job_instance.timestamps.get("deleted"))

    def test_deleted(self):
        job_instance = self.test_new_to_started()
        job_instance.cleanup()
        self.assertIsNotNone(job_instance.timestamps.get("cleanup"))
