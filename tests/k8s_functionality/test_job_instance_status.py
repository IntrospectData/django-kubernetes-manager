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

    def test_create_job_no_config_map_class_method_cleanup(self, job_instance=None):
        job_instance = job_instance or JobInstanceFactory(cluster=self.cluster, job_definition=self.job_definition)
        api_response = job_instance.job.create()
        self.assertIsNotNone(api_response)
        self.assertIsNotNone(api_response.metadata.creation_timestamp)
        job_instance.cleanup()
        self.assertIsNotNone(job_instance.timestamps.get("cleanup"))
        self.assertTrue(job_instance.is_complete)

    def test_create_job_with_config_map_class_method_cleanup(self, job_instance=None):
        job_instance = self._get_job_instance(
            job_instance=job_instance or JobInstanceFactory(cluster=self.cluster, job_definition=self.job_definition, script="#!/bin/bash\nls -shall")
        )
        api_response = job_instance.job.create()
        self.assertIsNotNone(api_response)
        self.assertIsNotNone(api_response.metadata.creation_timestamp)
        self.assertIsNotNone(job_instance.config_map.read())
        job_instance.cleanup()
        self.assertIsNotNone(job_instance.timestamps.get("cleanup"))
        self.assertTrue(job_instance.is_complete)
