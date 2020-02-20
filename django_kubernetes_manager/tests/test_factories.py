from test_plus.test import TestCase

from .factories import *


class FactoryTestCase(TestCase):
    def test_job_definition(self):
        obj = JobDefinitionFactory()
        self.assertIsNotNone(obj)

    def test_job_instance(self):
        obj = JobInstanceFactory()
        self.assertIsNotNone(obj)

    def test_telemetry_entry(self):
        obj = TelemetryEntryFactory()
        self.assertIsNotNone(obj)

    def test_log_entry(self):
        obj = LogEntryFactory()
        self.assertIsNotNone(obj)

    def test_target_cluster(self):
        obj = TargetClusterFactory()
        self.assertIsNotNone(obj)
