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
class K8sConfigMapTestCase(BaseJobCleanupTestCase):
    # fixtures = []

    def test_config_map_exists(self, job_instance=None):
        job_instance = self._get_job_instance(
            job_instance=job_instance or JobInstanceFactory(cluster=self.cluster, job_definition=self.job_definition, script="#!/bin/bash\nls -shall")
        )
        self.assertIsNotNone(job_instance.config_map.build())

    def test_config_map_not_exists(self, job_instance=None):
        job_instance = self._get_job_instance(job_instance=job_instance)
        self.assertIsNone(job_instance.config_map.build())

    def test_create_config_map(self, job_instance=None):
        job_instance = self._get_job_instance(
            job_instance=job_instance or JobInstanceFactory(cluster=self.cluster, job_definition=self.job_definition, script="#!/bin/bash\nls -shall")
        )
        cm = job_instance.config_map.build()
        with job_instance.get_k8s_client() as api_client:
            api_response = api_client.create_namespaced_config_map(body=cm, namespace=job_instance.namespace)
            self.assertIsNotNone(api_response)
            self.assertIsNotNone(api_response.metadata.creation_timestamp)
        return api_response

    def test_create_config_map_class_method(self, job_instance=None):
        job_instance = self._get_job_instance(
            job_instance=job_instance or JobInstanceFactory(cluster=self.cluster, job_definition=self.job_definition, script="#!/bin/bash\nls -shall")
        )
        api_response = job_instance.config_map.create()
        self.assertIsNotNone(api_response)
        self.assertIsNotNone(api_response.metadata.creation_timestamp)
        return job_instance

    def test_read_config_map(self, job_instance=None):
        job_instance = self._get_job_instance(job_instance=job_instance or self.test_create_config_map_class_method(job_instance=job_instance))
        r = job_instance.config_map.read()
        self.assertIsNotNone(r)
        self.assertTrue(r.metadata.name == str(job_instance.id))

    def test_delete_config_map(self, job_instance=None):
        job_instance = self._get_job_instance(job_instance=job_instance or self.test_create_config_map_class_method(job_instance=job_instance))
        r = job_instance.config_map.delete()
        self.assertTrue(r)
        self.assertIsNone(job_instance.config_map.read())
