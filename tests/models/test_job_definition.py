from test_plus.test import TestCase
from k8s_job.models import JobDefinition


# Create your tests here.
class JobDefinitionTestCase(TestCase):
    # fixtures = []

    # def setUp(self):
    #     pass

    def test_create_object(self, **kwargs):
        if "image_name" not in kwargs:
            kwargs["image_name"] = "nginx"
        if "image_tag" not in kwargs:
            kwargs["image_tag"] = "latest"
        jd, created = JobDefinition.objects.get_or_create(**kwargs)
        self.assertTrue(created)
        for k in ["id", "lineage_id"]:
            self.assertIsNotNone(getattr(jd, k, None))
        for k, v in kwargs.items():
            self.assertTrue(getattr(jd, k, None) == v)
        return jd

    def test_lineage_id(self, **kwargs):
        jd = self.test_create_object(**kwargs)
        lineage_id = jd.lineage_id
        id = jd.pk
        jd.save()
        jd.refresh_from_db()
        self.assertTrue(jd.lineage_id == lineage_id)
        self.assertTrue(jd.pk != id)
