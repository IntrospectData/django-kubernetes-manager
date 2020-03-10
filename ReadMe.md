# Django Kubernetes Manager

Control multiple Kubernetes clusters and resources using Django Rest Framework.

## Installation

### From Pip

```bash
  $ pip install django_kubernetes_manager
```

### From source
```bash
  $ git clone https://github.com/IntrospectData/Django-kubernetes-manager
  $ cp django_kubernetes_manager /my/django/project/dkm
```


## Current Models

TargetCluster

KubernetesContainer

KubernetesVolume

KubernetesVolumeMount

KubernetesPodTemplate

KubernetesDeployment

KubernetesJob

KubernetesService

KubernetesIngress

KubernetesNamespace

## API Docs

```bash
  ./manage.py runserver
```

*See http(s)://localhost:8000/api/redoc for documentation*
