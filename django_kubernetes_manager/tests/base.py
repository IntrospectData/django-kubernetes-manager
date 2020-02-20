import hashlib
import time
from datetime import datetime

import yaml

from test_plus.test import TestCase
from k8s_job.models import JobInstance, TargetCluster
from k8s_job.tests.factories import JobDefinitionFactory, JobInstanceFactory, TargetClusterFactory
from k8s_job.utils import get_command_output, log
from kubernetes import client


# Create your tests here.
class BaseJobCleanupTestCase(TestCase):
    # fixtures = []
    def setUp(self):
        self.job_definition = JobDefinitionFactory(image_name="introspectdata/k8s-test", image_tag="latest")
        self.kubeconfig = get_command_output("microk8s.kubectl config view --raw=true")
        self.cluster = TargetCluster.add(self.kubeconfig)[0]
        self.jobs = []

    def _get_job_instance(self, job_instance=None):
        ret_val = job_instance or JobInstanceFactory(cluster=self.cluster, job_definition=self.job_definition)
        self.jobs.append(ret_val)
        return ret_val

    def tearDown(self):
        for job in self.jobs:
            try:
                job.cleanup()
            except:
                log.info("Job is already gone...")
