from django.conf.urls import url
from django.contrib import admin
from django.urls import include, path
from kubernetes_manager import views
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions, routers

schema_view = get_schema_view(
    openapi.Info(
        title="DKM API",
        default_version="v0.1.0",
        description="Django Kubernetes Manager",
        contact=openapi.Contact(email="bradley@introspectdata.com"),
        license=openapi.License(name="MIT License", url="https://github.com/IntrospectData/Django-Kubernetes-Manager/blob/master/LICENSE"),
    ),
    public=True,
    permission_classes=(permissions.IsAuthenticated,),
)

router = routers.DefaultRouter()
router.register(r"containers", views.KubernetesContainerViewSet)
router.register(r"pods", views.KubernetesPodTemplateViewSet)
router.register(r"deployments", views.KubernetesDeploymentViewSet)
router.register(r"services", views.KubernetesServiceViewSet)
router.register(r"ingresses", views.KubernetesIngressViewSet)
router.register(r"jobs", views.KubernetesJobViewSet)
router.register(r"clusters", views.TargetClusterViewSet)
router.register(r"namespaces", views.KubernetesNamespaceViewSet)
router.register(r"configmaps", views.KubernetesConfigMapViewSet)
router.register(r"volumes", views.KubernetesVolumeViewSet)
router.register(r"mounts", views.KubernetesVolumeMountViewSet)


urlpatterns = [
    path("api/", include(router.urls)),
    path("api/auth/", include("rest_framework.urls", namespace="rest")),
    url(r"^api/swagger(?P<format>\.json|\.yaml)$", schema_view.without_ui(cache_timeout=0), name="schema-json"),
    path("api/swagger/", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    path("api/redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
]
