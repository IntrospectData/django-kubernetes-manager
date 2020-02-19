import os

import factory
from test_plus.test import TestCase
from k8s_job.models import TargetCluster

from .. import DATA_DIR


class TargetClusterTestCase(TestCase):
    # fixtures = []
    # def setUp(self):
    #     pass

    def test_create_object(self, **kwargs):
        if "title" not in kwargs:
            kwargs["title"] = "This is a title"
        if "description" not in kwargs:
            kwargs["description"] = ""
        if "config" not in kwargs:
            kwargs["config"] = {"this": "is"}
        if "api_endpoint" not in kwargs:
            kwargs["api_endpoint"] = factory.Faker("url").generate()
        if "telemetry_endpoint" not in kwargs:
            kwargs["telemetry_endpoint"] = factory.Faker("url").generate()
        obj = TargetCluster.objects.create(**kwargs)
        for k in ["id"]:
            self.assertIsNotNone(getattr(obj, k, None))
        for k, v in kwargs.items():
            self.assertTrue(getattr(obj, k, None) == v)
        return obj

    def test_config(self, **kwargs):
        kwargs["title"] = "this is another title"
        kwargs["config"] = {"vertical_1": "owl", "horizontal_1": "grasshopper", "vertical_2": "flamingo", "vertical_3": "mouse", "horizontal_2": "dog"}
        obj = self.test_create_object(**kwargs)
        for k in list(kwargs["config"].keys()):
            self.assertTrue(k in obj.config)

    def test_credential_add(self):
        with open(os.path.join(DATA_DIR, "microk8s-kubeconfig"), "r") as f:
            input_txt = f.read()
        obj = TargetCluster.add(input_txt)
        self.assertIsNotNone(obj)
        return obj
