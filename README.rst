
.. image:: images/dkm-logo.png
   :width: 600
   : DjangoKubernetesManager
   
Django Kubernetes Manager is a Django app that enables you to control a
a Kubernetes cluster using the Python API and Django Rest Framework.

License
--------
This project is license under the MIT license. Please see the license dir for
dependency licenses.

Docs
-------
API_
Full_


.. _API: https://github.com/IntrospectData/Django-Kubernetes-Manager/blob/master/docs/openapi.md

.. _Full: https://django-kubernetes-manager.readthedocs.io/en/latest/index.html


Installation
---------------
Install the app using pip::

  $ pip install django-kubernetes-manager

Getting Started
---------------
1. Add "django_kubernetes_manager" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'django_kubernetes_manager',
    ]

2. Include the django_kubernetes_manager URLconf in your project urls.py like this::

    path('dkm/', include('django_kubernetes_manager.urls')),

3. Run ``python manage.py migrate`` to create the models in your database.
    * Requires Postgresql or other database with JSON support.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to configure a TargetCluster (you'll need the Admin app enabled).

5. Create, update, delete, deploy, or remove a Kubernetes object
   using the api :)
