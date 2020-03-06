"""dkm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django_kubernetes_manager import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'containers', views.KubernetesContainerViewSet)
router.register(r'pods', views.KubernetesPodTemplateViewSet)
router.register(r'deployments', views.KubernetesDeploymentViewSet)
router.register(r'services', views.KubernetesServiceViewSet)
router.register(r'ingresses', views.KubernetesIngressViewSet)
router.register(r'jobs', views.KubernetesJobViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest')),
    path('admin/', admin.site.urls),
]
