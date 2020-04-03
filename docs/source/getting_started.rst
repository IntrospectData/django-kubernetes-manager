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
    django_kubernetes_manager,
  ]

* In urls.py include the package urls

.. code-block:: python

  urlpatterns = [
    ... ,
    path('dkm/', include('django_kubernetes_manager.urls')),
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
