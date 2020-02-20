import random
from datetime import timedelta

from test_plus.test import TestCase
from django.utils import timezone
from factory import Faker
from k8s_job.models import JobInstance, TelemetryEntry
from k8s_job.tests.factories import JobInstanceFactory

TEST_METRIC_KEYS = ["metric1", "metric2", "metric3"]


def generate_data():
    return {k: random.random() * 100 for k in TEST_METRIC_KEYS}


# Create your tests here.
class TelemetryEntryTestCase(TestCase):
    # fixtures = []

    def setUp(self):
        self.job_instance = JobInstanceFactory()

    def assert_kwargs(self, obj, kwargs):
        for k, v in kwargs.items():
            if isinstance(v, dict):
                for kk, vv in v.items():
                    self.assertTrue(getattr(obj, k, {})[kk] == vv)
            elif not isinstance(v, JobInstance):
                self.assertTrue(getattr(obj, k, None) == v)

    def test_create_object(self, **kwargs):
        if "job_instance" not in kwargs:
            kwargs["job_instance"] = self.job_instance
        if "data" not in kwargs:
            kwargs["data"] = generate_data()
        te = TelemetryEntry(**kwargs)
        te.save()
        for k in ["id"]:
            self.assertIsNotNone(getattr(te, k, None))
        self.assert_kwargs(te, kwargs)
        self.assertIsNotNone(te.data_hash)
        return te

    def test_telemetry_add(self, **kwargs):
        if "job_instance" not in kwargs:
            kwargs["job_instance"] = self.job_instance
        if "data" not in kwargs:
            kwargs["data"] = generate_data()
        te = TelemetryEntry.add(**kwargs)
        for k in ["id"]:
            self.assertIsNotNone(getattr(te, k, None))
        self.assert_kwargs(te, kwargs)
        self.assertIsNotNone(te.data_hash)
        return te

    def test_metric_from_instance(self, **kwargs):
        if "data" not in kwargs:
            kwargs["data"] = generate_data()
        ret_val = self.job_instance.add_metric(**kwargs)
        self.assertTrue(ret_val)
        return ret_val

    def test_metric_deduplication(self):
        t1 = timezone.now() - timedelta(hours=24)
        t2 = timezone.now() - timedelta(hours=12)
        t3 = timezone.now() - timedelta(hours=6)
        d1 = generate_data()
        d2 = generate_data()
        d3 = d2.copy()
        te1 = TelemetryEntry.add(job_instance=self.job_instance, data=d1, as_of=t1)
        te2 = TelemetryEntry.add(job_instance=self.job_instance, data=d2, as_of=t2)
        teN = TelemetryEntry.add(job_instance=self.job_instance, data=d3, as_of=t3)
        self.assertIsNone(teN)
