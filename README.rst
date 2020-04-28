.. image:: https://circleci.com/gh/IntrospectData/django-kubernetes-manager.svg?style=shield
    :target: https://circleci.com/gh/IntrospectData/django-kubernetes-manager


.. image:: https://api.codeclimate.com/v1/badges/c866017f9bd481a3c9ca/maintainability
   :target: https://codeclimate.com/github/IntrospectData/django-kubernetes-manager/maintainability
   :alt: Maintainability


.. image:: https://api.codeclimate.com/v1/badges/c866017f9bd481a3c9ca/test_coverage
   :target: https://codeclimate.com/github/IntrospectData/django-kubernetes-manager/test_coverage
   :alt: Test Coverage


.. image:: images/dkm-logo.png
   :width: 500
   :alt: DjangoKubernetesManager


=================================
Django Kubernetes Manager 0.4.6
=================================

Django Kubernetes Manager is an open source project to wrap the complexity of Kubernetes management in the simplicity of Django Rest Framework.

Introduction
-------------

Our engineering team has developed several data processing apps, and
found celery wasn't quite enough for dispatching heavier tasks.
We decided to try Kubernetes Jobs, and while pleased with performance,
wanted a less verbose, more object oriented way to interact with our clusters.

And thus Django Kubernetes Manager was spawned. Using Django Rest Framework and
the kubernetes client library, our devs came up with the idea to treat each object
we'd be deploying as a Model instance, and use the DRF viewsets and actions to
create an RESTful API framework from which we could extend for each projects
particular needs.


License
--------
This project is license under the MIT license.


Please see the license dir for dependency licenses.

Docs
-------
ReadTheDocs_

.. _ReadTheDocs: https://django-kubernetes-manager.readthedocs.io/en/latest/index.html

Installation
---------------
Install the app using pip::

  $ pip install django-kubernetes-manager

Getting Started
---------------
1. Add "kubernetes_manager" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'kubernetes_manager',
    ]

2. Include the kubernetes_manager URLconf in your project urls.py like this::

    path('dkm/', include('kubernetes_manager.urls')),

3. To create models in your database, run::

    python manage.py migrate

    * Requires Postgresql or other database with JSON support.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to configure a TargetCluster (you'll need the Admin app enabled).

5. Create, update, delete, deploy, or remove a Kubernetes object
   using the api :)
