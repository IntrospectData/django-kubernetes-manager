from datetime import timedelta

from test_plus.test import TestCase
from django.utils import timezone
from factory import Faker
from k8s_job.models import LogEntry
from k8s_job.tests.factories import JobDefinitionFactory, JobInstanceFactory


# Create your tests here.
class LogEntryTestCase(TestCase):
    # fixtures = []

    def setUp(self):
        self.job_definition = JobDefinitionFactory()
        self.job_instance = JobInstanceFactory(job_definition=self.job_definition)

    def test_create_object(self, **kwargs):
        if "job_instance" not in kwargs:
            kwargs["job_instance"] = self.job_instance
        if "message" not in kwargs:
            kwargs["message"] = Faker("sentence").generate()
        le = LogEntry.objects.create(**kwargs)
        for k in ["id"]:
            self.assertIsNotNone(getattr(le, k, None))
        for k, v in kwargs.items():
            self.assertTrue(getattr(le, k, None) == v)
        return le

    def test_log_from_instance(self, **kwargs):
        if "message" not in kwargs:
            kwargs["message"] = Faker("sentence").generate()
        ret_val = self.job_instance.add_log(**kwargs)
        self.assertTrue(ret_val)
        return ret_val
