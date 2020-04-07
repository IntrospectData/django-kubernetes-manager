import random
import string

from django.test import TestCase

from .factories import (
    KubernetesConfigMapFactory,
    KubernetesContainerFactory,
    KubernetesDeploymentFactory,
    KubernetesJobFactory,
    KubernetesNamespaceFactory,
    KubernetesPodTemplateFactory,
    KubernetesVolumeFactory,
    KubernetesVolumeMountFactory,
    TargetClusterFactory,
)


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

    def namespace_create_api(self):
        arf = APIRequestFactory()
        req = arf.post(
            "/namespaces/",
            {
                "title": str(factory.fuzzy.FuzzyText()),
                "description": str(factory.fuzzy.FuzzyText()),
                "cluster": "http://127.0.0.1:8000/dkm/api/clusters/1/",
                "labels": {"app": "test"},
                "annotations": {"type": "project"},
                "api_version": "v1",
                "kind": "Namespace",
                "exists": False,
            },
        )

    def namespace_deploy_api(self):
        arf = APIRequestFactory()
        req = arf.get("/namespaces/{}/deploy".format(id))

    def namespace_remove_api(self):
        arf = APIRequestFactory()
        req = arf.get("/namespaces/{}/remove".format(id))

    def namespace_delete_api(self):
        arf = APIRequestFactory()
        req = arf.delete("/namespaces/{}/".format(id))


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
        rstr = ''.join(random.choices(string.ascii_lowercase + string.digits, k = 7))
        obj = KubernetesPodTemplateFactory(
            containers=(
                KubernetesContainerFactory(title=rstr), KubernetesContainerFactory(title=rstr+"-2")
            ),
            volumes=(
                KubernetesVolumeFactory(title=rstr), KubernetesVolumeFactory(title=rstr+"-2")
            )
        )
        self.assertIsNotNone(obj)
        self.assertIsNotNone(obj.pk)

    def test_get_obj(self):
        obj = KubernetesPodTemplateFactory(
            containers=(
                KubernetesContainerFactory(), KubernetesContainerFactory()
            )
        )
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
