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



class KubernetesNamespaceTestCase(TestCase):

    def test_model(self):
        obj = KubernetesNamespaceFactory()
        self.assertIsNotNone(obj)
        self.assertIsNotNone(obj.pk)

    def test_get_obj(self):
        obj = KubernetesNamespaceFactory()
        obj = obj.get_obj()
        self.assertIsNotNone(obj)

    def test_api(self):
        pass



class KubernetesVolumeTestCase(TestCase):

    def test_model(self):
        obj = KubernetesVolumeFactory()
        self.assertIsNotNone(obj)
        self.assertIsNotNone(obj.pk)

    def test_get_obj(self):
        obj = KubernetesVolumeFactory()
        obj = obj.get_obj()
        self.assertIsNotNone(obj)

    def test_api(self):
        pass



class KubernetesVolumeMountTestCase(TestCase):

    def test_model(self):
        obj = KubernetesVolumeMountFactory()
        self.assertIsNotNone(obj)
        self.assertIsNotNone(obj.pk)

    def test_get_obj(self):
        obj = KubernetesVolumeMountFactory()
        obj = obj.get_obj()
        self.assertIsNotNone(obj)

    def test_api(self):
        pass



class KubernetesConfigMapTestCase(TestCase):

    def test_model(self):
        obj = KubernetesConfigMapFactory()
        self.assertIsNotNone(obj)
        self.assertIsNotNone(obj.pk)

    def test_get_obj(self):
        obj = KubernetesConfigMapFactory()
        obj = obj.get_obj()
        self.assertIsNotNone(obj)

    def test_api(self):
        pass



class KubernetesContainerTestCase(TestCase):

    def test_model(self):
        obj = KubernetesContainerFactory()
        self.assertIsNotNone(obj)
        self.assertIsNotNone(obj.pk)

    def test_get_obj(self):
        obj = KubernetesContainerFactory()
        obj = obj.get_obj()
        self.assertIsNotNone(obj)

    def test_api(self):
        pass



class KubernetesPodTemplateTestCase(TestCase):

    def test_model(self):
        obj = KubernetesPodTemplateFactory()
        self.assertIsNotNone(obj)
        self.assertIsNotNone(obj.pk)

    def test_get_obj(self):
        obj = KubernetesPodTemplateFactory()
        obj = obj.get_obj()
        self.assertIsNotNone(obj)

    def test_api(self):
        pass



class KubernetesDeploymentTestCase(TestCase):

    def test_model(self):
        obj = KubernetesDeploymentFactory()
        self.assertIsNotNone(obj)
        self.assertIsNotNone(obj.pk)

    def test_get_obj(self):
        obj = KubernetesDeploymentFactory()
        obj = obj.get_obj()
        self.assertIsNotNone(obj)

    def test_api(self):
        pass



class KubernetesJobTestCase(TestCase):

    def test_model(self):
        obj = KubernetesJobFactory()
        self.assertIsNotNone(obj)
        self.assertIsNotNone(obj.pk)

    def test_get_obj(self):
        obj = KubernetesJobFactory()
        obj = obj.get_obj()
        self.assertIsNotNone(obj)

    def test_api(self):
        pass
