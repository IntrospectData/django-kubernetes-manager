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


class K8sJobWithConfigMapTestCase(BaseJobCleanupTestCase):
    def test_create_job_with_config_map(self, job_instance=None):
        job_instance = job_instance or JobInstanceFactory(cluster=self.cluster, job_definition=self.job_definition, script="#!/bin/bash\nls -shall")
        with job_instance.get_k8s_client() as cm_client, job_instance.get_k8s_client(client.BatchV1Api) as api_client:
            cm_response = cm_client.create_namespaced_config_map(body=job_instance.config_map.build(), namespace=job_instance.namespace)
            self.assertIsNotNone(cm_response)
            self.assertIsNotNone(cm_response.metadata.creation_timestamp)
            api_response = api_client.create_namespaced_job(body=job_instance.job.build(), namespace=job_instance.namespace)
            self.assertIsNotNone(api_response)
            self.assertIsNotNone(api_response.metadata.creation_timestamp)
        self.assertIsNotNone(job_instance.config_map.read())
        return api_response

    def test_create_job_with_config_map_class_method(self, job_instance=None):
        job_instance = job_instance or JobInstanceFactory(cluster=self.cluster, job_definition=self.job_definition, script="#!/bin/bash\nls -shall")
        api_response = job_instance.job.create()
        self.assertIsNotNone(api_response)
        self.assertIsNotNone(api_response.metadata.creation_timestamp)
        self.assertIsNotNone(job_instance.config_map.read())
        return job_instance

    def test_read_job_with_config_map(self, job_instance=None):
        job_instance = self.test_create_job_with_config_map_class_method(job_instance=job_instance)
        r = job_instance.job.read()
        self.assertIsNotNone(r)
        self.assertTrue(r.metadata.name == str(job_instance.id))
        return job_instance

    def test_delete_job_with_config_map(self, job_instance=None):
        job_instance = self.test_create_job_with_config_map_class_method(job_instance=job_instance)
        loops = 0

        while not job_instance.job.read().status.succeeded and loops < 10:
            loops += 1
            time.sleep(5)

        r = job_instance.job.delete()
        self.assertTrue(r)
        self.assertIsNone(job_instance.config_map.read())
        self.assertIsNone(job_instance.job.read())
