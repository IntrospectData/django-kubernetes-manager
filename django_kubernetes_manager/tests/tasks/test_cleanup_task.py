import hashlib
import time
from datetime import datetime

import yaml
from kubernetes import client
from test_plus.test import TestCase

import k8s_job.utils as utils
from k8s_job.models import JobInstance, TargetCluster
from k8s_job.tasks.cleanup import cleanup_job
from k8s_job.tests.factories import JobDefinitionFactory, JobInstanceFactory, TargetClusterFactory

from ..base import BaseJobCleanupTestCase


# Create your tests here.
class JobInstanceCleanupTestCase(BaseJobCleanupTestCase):
    # def test_cleanup_job_task(self, job_instance=None):
    #     job_instance = self._get_job_instance(job_instance=job_instance)
    #     api_response = job_instance.job.create()
    #     self.assertIsNotNone(api_response)
    #     self.assertIsNotNone(api_response.metadata.creation_timestamp)
    #     loops = 0
    #     while not job_instance.job.read().status.succeeded and loops < 120:
    #         utils.log.debug(job_instance.job.read().status)
    #         loops += 1
    #         time.sleep(2)
    #
    #     self.assertTrue(cleanup_job(job_instance_id=str(job_instance.id)))

    def test_cleanup_job_task_fails(self, job_instance=None):
        job_instance = self._get_job_instance(job_instance=job_instance)
        api_response = job_instance.job.create()
        self.assertIsNotNone(api_response)
        self.assertIsNotNone(api_response.metadata.creation_timestamp)
        job_instance.cleanup()
        self.assertFalse(cleanup_job(job_instance_id=str(job_instance.id)))
