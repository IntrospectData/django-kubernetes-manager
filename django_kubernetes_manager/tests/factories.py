import random

import factory
import factory.fuzzy
from coolname import generate_slug
from factory.django import DjangoModelFactory
from k8s_job.models import JobDefinition, JobInstance, LogEntry, TargetCluster, TelemetryEntry


def fake_json(number):
    """Fake dictionary generator with sequence built-in"""
    ret_val = {}
    for item in range(0, random.randint(3, 6)):
        ret_val[generate_slug(2)] = "value {}".format(number)
    return ret_val


def fake_metric(number=1):
    """Fake dictionary generator with sequence for generating metrics"""
    ret_val = {}
    for item in range(0, random.randint(3, 6)):
        ret_val[generate_slug(2)] = random.random() * number
    return ret_val


class TargetClusterFactory(DjangoModelFactory):
    title = factory.Faker("bs")
    description = factory.Faker("catch_phrase")
    api_endpoint = factory.Faker("url")
    telemetry_endpoint = factory.Faker("url")
    config = factory.Sequence(fake_json)

    class Meta:
        model = TargetCluster


class JobDefinitionFactory(DjangoModelFactory):

    title = factory.Faker("bs")
    description = factory.Faker("catch_phrase")
    image_name = "introspectdata/k8s-test"
    config = factory.Sequence(fake_json)

    class Meta:
        model = JobDefinition


class JobInstanceFactory(DjangoModelFactory):

    notes = factory.Faker("paragraphs")
    job_definition = factory.SubFactory(JobDefinitionFactory)
    config = factory.Sequence(fake_json)
    cluster = factory.SubFactory(TargetClusterFactory)

    class Meta:
        model = JobInstance


class TelemetryEntryFactory(DjangoModelFactory):

    data = factory.Sequence(fake_metric)
    job_instance = factory.SubFactory(JobInstanceFactory)

    class Meta:
        model = TelemetryEntry


class LogEntryFactory(DjangoModelFactory):

    message = factory.Faker("sentence")

    class Meta:
        model = LogEntry
