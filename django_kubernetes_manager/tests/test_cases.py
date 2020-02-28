from django.test import TestCase
from .factories import KubernetesDeploymentFactory, KubernetesJobFactory



class KubernetesDeploymentTestCase(TestCase):

    def test_model(self):
        dep = KubernetesDeploymentFactory()
        self.assertIsNotNone(dep)
        self.assertIsNotNone(dep.pk)

    def test_get_obj(self):
        dep = KubernetesDeploymentFactory()
        obj = dep.get_obj()
        self.assertIsNotNone(obj)



class KubernetesJobTestCase(TestCase):

    def test_model(self):
        job = KubernetesJobFactory()
        self.assertIsNotNone(job)
        self.assertIsNotNone(job.pk)

    def test_get_obj(self):
        job = KubernetesJobFactory()
        obj = job.get_obj()
        self.assertIsNotNone(obj)
