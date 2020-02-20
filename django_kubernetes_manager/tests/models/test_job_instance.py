from test_plus.test import TestCase
from k8s_job.models import JobInstance
from k8s_job.tests.factories import JobDefinitionFactory, JobInstanceFactory, TargetClusterFactory
from kubernetes import client


# Create your tests here.
class JobInstanceTestCase(TestCase):
    # fixtures = []

    def test_create_object(self, **kwargs):
        if "job_definition" not in kwargs:
            job_definition = JobDefinitionFactory()
            job_definition.save()
            kwargs["job_definition"] = job_definition
        if not "cluster" in kwargs:
            cluster = kwargs["job_definition"].cluster
            if not cluster:
                cluster = TargetClusterFactory()
            kwargs["cluster"] = cluster
        ji = JobInstance.objects.create(**kwargs)
        for k in ["id"]:
            self.assertIsNotNone(getattr(ji, k, None))
        for k, v in kwargs.items():
            self.assertTrue(getattr(ji, k, None) == v)
        return ji

    def test_build_k8s_container(self, ji=None):
        ji = ji or self.test_create_object()
        container = ji.job.build_k8s_container()
        self.assertIsNotNone(container)
        self.assertTrue(isinstance(container, client.V1Container))
        return container

    def test_build_k8s_container_config_jd_override(self):
        definition_config = {"container": {"image": "definition_config", "image_pull_policy": "definition_tag", "args": "df -sh", "command": "/bin/sh"}}
        jd1 = JobDefinitionFactory(config=definition_config)
        ji = JobInstanceFactory(job_definition=jd1)
        container = ji.job.build_k8s_container()
        for k, v in definition_config.get("container", {}).items():
            if isinstance(getattr(container, k, None), list):
                self.assertTrue(" ".join(getattr(container, k, None)) == v.strip())
            else:
                self.assertTrue(getattr(container, k, None) == v)

    def test_build_k8s_container_config_ji_override(self):
        instance_config = {"container": {"image": "instance-image", "image_pull_policy": "instance-tag", "args": "ls -all", "command": "/bin/bash"}}
        ji = JobInstanceFactory(config=instance_config)
        container = ji.job.build_k8s_container()
        for k, v in instance_config.get("container", {}).items():
            if isinstance(getattr(container, k, None), list):
                self.assertTrue(" ".join(getattr(container, k, None)) == v.strip())
            else:
                self.assertTrue(getattr(container, k, None) == v)

    def test_build_k8s_template(self, ji=None):
        ji = ji or self.test_create_object()
        container = self.test_build_k8s_container(ji=ji)
        template = ji.job.build_k8s_template(container=container)
        self.assertIsNotNone(template)
        self.assertTrue(isinstance(template, client.V1PodTemplateSpec))
        return template

    def test_build_k8s_template_containers(self, ji=None):
        ji = ji or self.test_create_object()
        container = self.test_build_k8s_container(ji=ji)
        template = ji.job.build_k8s_template(containers=[container])
        self.assertIsNotNone(template)
        self.assertTrue(isinstance(template, client.V1PodTemplateSpec))
        return template

    def test_build_k8s_job_spec(self, ji=None):
        ji = ji or self.test_create_object()
        template = self.test_build_k8s_template(ji=ji)
        spec = ji.job.build_k8s_job_spec(template=template)
        self.assertIsNotNone(spec)
        self.assertTrue(isinstance(spec, client.V1JobSpec))
        return spec

    def test_build_k8s_job(self, ji=None):
        ji = ji or self.test_create_object()
        spec = self.test_build_k8s_job_spec(ji=ji)
        job = ji.job.build_k8s_job(job_spec=spec)
        self.assertIsNotNone(job)
        self.assertTrue(isinstance(job, client.V1Job))

    def test_build(self, ji=None):
        ji = ji or self.test_create_object()
        job = ji.job.build()
        self.assertIsNotNone(job)
        self.assertTrue(isinstance(job, client.V1Job))
