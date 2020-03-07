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
from django.conf.urls import url
from django.contrib import admin
from django.urls import include, path

from django_kubernetes_manager import views
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions, routers

schema_view = get_schema_view(
   openapi.Info(
      title="DKM API",
      default_version='v0.1.0',
      description="Django Kubernetes Manager",
      terms_of_service="https://introspectdata.com/terms-service/",
      contact=openapi.Contact(email="bradley@introspectdata.com"),
      license=openapi.License(name="MIT License"),
   ),
   public=True,
   permission_classes=(permissions.IsAuthenticated,),
)

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
    url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
