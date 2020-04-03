from django.test import TestCase

from .factories import (KubernetesConfigMapFactory, KubernetesContainerFactory,
                        KubernetesDeploymentFactory, KubernetesJobFactory,
                        KubernetesPodTemplateFactory, KubernetesVolumeFactory,
                        KubernetesVolumeMountFactory, TargetClusterFactory,
                        KubernetesNamespaceFactory)



class TargetClusterTestCase(TestCase):

    def test_model(self):
        pass

    def test_api(self):
        pass



class KubernetesNamespaceFactory(TestCase):

    def test_model(self):
        pass

    def test_get_obj(self):
        pass

    def test_api(self):
        pass



class KubernetesVolumeTestCase(TestCase):

    def test_model(self):
        pass

    def test_get_obj(self):
        pass

    def test_api(self):
        pass



class KubernetesVolumeMountTestCase(TestCase):

    def test_model(self):
        pass

    def test_get_obj(self):
        pass

    def test_api(self):
        pass



class KubernetesConfigMapTestCase(TestCase):

    def test_model(self):
        pass

    def test_get_obj(self):
        pass

    def test_api(self):
        pass



class KubernetesContainerTestCase(TestCase):

    def test_model(self):
        pass

    def test_get_obj(self):
        pass

    def test_api(self):
        pass



class KubernetesPodTemplateTestCase(TestCase):

    def test_model(self):
        pass

    def test_get_obj(self):
        pass

    def test_api(self):
        pass



class KubernetesDeploymentTestCase(TestCase):

    def test_model(self):
        dep = KubernetesDeploymentFactory()
        self.assertIsNotNone(dep)
        self.assertIsNotNone(dep.pk)

    def test_get_obj(self):
        dep = KubernetesDeploymentFactory()
        obj = dep.get_obj()
        self.assertIsNotNone(obj)

    def test_api(self):
        pass



class KubernetesJobTestCase(TestCase):

    def test_model(self):
        job = KubernetesJobFactory()
        self.assertIsNotNone(job)
        self.assertIsNotNone(job.pk)

    def test_get_obj(self):
        job = KubernetesJobFactory()
        obj = job.get_obj()
        self.assertIsNotNone(obj)

    def test_api(self):
        pass
