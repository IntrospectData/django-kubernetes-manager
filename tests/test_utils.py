import yaml
from test_plus.test import TestCase

import k8s_job.utils as utils
from k8s_job.models import JobInstance, TargetCluster
from k8s_job.tests.factories import JobDefinitionFactory, JobInstanceFactory


class UtilsTestCase(TestCase):
    def setUp(self):
        self.kubeconfig = utils.get_command_output("microk8s.kubectl config view --raw=true")

    def test_run_command(self):
        ret_val = utils.run_command("ls -all")
        self.assertTrue(ret_val == 0)

    def test_get_command_output(self):
        ret_val = utils.get_command_output("ls -all")
        self.assertIsNotNone(ret_val)

    def test_get_dict_hash(self):
        ret_val = utils.get_dict_hash({"this": "is", "a": "test"})
        self.assertTrue(len(ret_val) == 32)

    def test_find_namespaced_pod(self, job_instance=None):
        cluster = TargetCluster.add(self.kubeconfig)[0]
        job_definition = JobDefinitionFactory(image_name="introspectdata/k8s-test", image_tag="latest")
        job_instance = job_instance or JobInstanceFactory(cluster=cluster, job_definition=job_definition)
        api_response = job_instance.job.create()
        self.assertIsNotNone(api_response)
        self.assertIsNotNone(api_response.metadata.creation_timestamp)
        with job_instance.get_k8s_client() as api_client:
            pod_names = utils.find_namespaced_pods(job_instance.namespace, job_name=str(job_instance.id), api_client=api_client)
            self.assertIsNotNone(pod_names)

    def test_kubeconfig_parse(self):
        kc = utils.split_kubeconfig(self.kubeconfig)
        self.assertIsNotNone(kc)
        self.assertTrue(len(kc) == 1)
