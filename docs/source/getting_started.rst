Getting Started
=====================

Quickstart
----------------------------------------------

* Install from PyPi

.. code-block:: bash

  pip install django-kubernetes-manager

* In settings.py (or module) add the app

.. code-block:: python

  INSTALLED_APPS = [
    ... ,
    rest_framework,
    kubernetes_manager,
  ]

* In urls.py include the package urls

.. code-block:: python

  urlpatterns = [
    ... ,
    path('dkm/', include('kubernetes_manager.urls')),
  ]

* Run migrations and start server

.. code-block:: bash

  ./manage.py migrate
  ./manage.py runserver

* Navigate to django admin and create a TargetCluster

* Sample request

.. code-block:: bash

  curl http://127.0.0.1:8000/dkm/api/namespaces/?format=json

.. code-block:: json

  [
    {
      "title": "veridian-dynamics-aerodynamic-bagels",
      "description": null,
      "cluster": "http://127.0.0.1:8000/dkm/api/clusters/1/?format=json",
      "config": {},
      "labels": {
        "project": "aerodynamic-bagels",
        "organization": "veridian-dynamics"
      },
      "annotations": {},
      "api_version": "v1",
      "kind": "Namespace",
      "exists": true
    }
  ]

Sample Use-cases
-----------------
* Creating a labelled namespace for a client project:

.. code-block:: python

  from kubernetes_manager.models import KubernetesNamespace, TargetCluster
  from django.db import models
  from django_extensions.models import TitleDescriptionModel

  class AppNamespace(TitleDescriptionModel):
    project = models.OneToOneField("client.Project", on_delete=models.CASCADE)
    organization = models.ForeignKey("client.Org", on_delete=models.CASCADE)
    cluster = models.ForeignKey("kubernetes_manager.TargetCluster", on_delete=models.CASCADE)
    namespace = models.ForeignKey("kubernetes_manager.KubernetesNamespace", null=True, blank=True, on_delete=models.CASCADE)
    status = models.CharField(max_length = 128, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.status == "{'phase': 'Active'}":
            self.namespace = KubernetesNamespace.objects.create(
                title = "ns-" + self.organization.slug + "-" + self.project.slug,
                cluster = self.cluster,
                labels = {"organization":self.organization.slug, "project": self.project.slug},
                kind = "Namespace"
            )
            self.status = self.namespace.deploy()
        super().save(*args, **kwargs)

    def remove(self, *args, **kwargs):
        self.status = self.namespace.k_delete()

    def delete(self, *args, **kwargs):
        self.remove()
        super().delete(*args, **kwargs)



* Creating a two-container deployment:

.. code-block:: python

  from kubernetes_manager.models import KubernetesNamespace, TargetCluster
  from django.db import models
  from django_extensions.models import TitleDescriptionModel

  from .ns import AppNamespace

  class FileServer(TitleDescriptionModel):
      name = models.CharField(max_length=128)
      organization = models.ForeignKey("client.Org", on_delete=models.CASCADE)
      project = models.ForeignKey("client.Project", on_delete=models.CASCADE)
      cluster = models.ForeignKey("kubernetes_manager.TargetCluster", on_delete=models.CASCADE)
      namespace = models.ForeignKey(AppNamespace, on_delete=models.CASCADE)
      file = models.ForeignKey("library.FileItem", on_delete=models.CASCADE)
      docker_image = models.CharField(max_length=256, help_text="Docker repo path for image")
      docker_tag = models.CharField(max_length=16, help_text="Docker tag for image")
      definition = JSONField(null=True, blank=True)

      # define volume
      def vol(self, *args, **kwargs):
          volume = KubernetesVolume.objects.create(
              title = self.name + "-vol",
              cluster = self.cluster
          )
          return volume

      # create primary container
      def container_spec(self, *args, **kwargs):
          container = KubernetesContainer.objects.create(
              title = self.name,
              cluster = self.cluster,
              image_name = self.docker_image,
              image_tag = self.docker_tag,
              volume_mount = KubernetesVolumeMount.objects.create(
                  title = self.name + "-vol",
                  cluster = self.cluster
              ) if not kwargs.get("mount", None) else kwargs.get("mount"),
              command = "ls",
              args ="/media"
          )
          return container

      # create download sidecar
      def sidecar_spec(self, *args, **kwargs):
          sidecar = KubernetesContainer.objects.create(
              title = self.name,
              cluster = self.cluster,
              image_name = "curlimages/curl",
              image_tag = "7.69.1",
              volume_mount = KubernetesVolumeMount.objects.create(
                  title = self.name + "-vol",
                  cluster = self.cluster
              ) if not kwargs.get("mount", None) else kwargs.get("mount"),
              command = "/bin/sh",
              args = '-c,curl -oL {} {}'.format(self.file.name, self.file.url)
          )
          return sidecar

      # create pod template
      def pod_template_spec(self, *args, **kwargs):
          volume_mount = KubernetesVolumeMount.objects.create(
              title = self.name + "-vol",
              cluster = self.cluster
          )
          pod = KubernetesPodTemplate.objects.create(
              title = self.name,
              cluster = self.cluster,
              volume = self.vol(),
              primary_container = self.container_spec(mount=volume_mount),
              secondary_container = self.sidecar_spec(mount=volume_mount),
              restart_policy = "Always",
              labels = {"project": self.project.slug}
          )
          return pod

      # tie it up and deplioy
      def deploy(self):
          pod = self.pod_template_spec()
          deployment = KubernetesDeployment.objects.create(
              title = self.name,
              cluster = self.cluster,
              api_version = "apps/v1",
              kind = "Deployment",
              namespace = self.namespace.namespace.slug,
              labels = {"project": self.project.slug},
              selector = {"project": self.project.slug},
              pod_template = pod
          )
          self.definition = deployment.get_obj().to_dict()
          self.save()
          return deployment.deploy()
