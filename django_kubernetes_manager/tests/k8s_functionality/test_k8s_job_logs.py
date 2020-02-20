import hashlib
import time
from datetime import datetime

import yaml
from kubernetes import client
from test_plus.test import TestCase

import k8s_job.utils as utils
from k8s_job.models import JobInstance, LogEntry, TargetCluster
from k8s_job.tests.factories import JobDefinitionFactory, JobInstanceFactory, TargetClusterFactory

from ..base import BaseJobCleanupTestCase


# Create your tests here.
class K8sJobLogsTestCase(BaseJobCleanupTestCase):
    # fixtures = []
    def test_create_job_find_logs(self, job_instance=None):
        job_instance = self._get_job_instance(job_instance=job_instance)
        api_response = job_instance.job.create()
        self.assertIsNotNone(api_response)
        self.assertIsNotNone(api_response.metadata.creation_timestamp)
        loops = 0
        utils.log.debug(job_instance.id)
        while not job_instance.job.read().status.succeeded and loops < 120:
            utils.log.debug(job_instance.job.read().status)
            loops += 1
            time.sleep(2)

        logs = job_instance.job.get_job_logs()
        self.assertIsNotNone(logs)
        job_instance.refresh_from_db()
        self.assertTrue(LogEntry.objects.filter(job_instance=job_instance).count() > 0)
