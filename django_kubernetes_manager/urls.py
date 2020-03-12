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
      license=openapi.License(
        name="MIT License",
        url="https://github.com/IntrospectData/Django-Kubernetes-Manager/blob/master/LICENSE"
      ),
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
router.register(r'clusters', views.TargetClusterViewSet)
router.register(r'namespaces', views.KubernetesNamespaceViewSet)

urlpatterns = [
    path('dkm/', include(router.urls)),
    path('dkm/auth/', include('rest_framework.urls', namespace='rest')),
    url(r'^dkm/swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('dkm/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('dkm/redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
