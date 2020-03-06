from .models import (KubernetesContainer, KubernetesDeployment,
                    KubernetesIngress, KubernetesJob, KubernetesPodTemplate,
                    KubernetesService)
from rest_framework import permissions, viewsets

from .serializers import (KubernetesContainerSerializer,
                          KubernetesDeploymentSerializer,
                          KubernetesIngressSerializer, KubernetesJobSerializer,
                          KubernetesPodTemplateSerializer,
                          KubernetesServiceSerializer)



class KubernetesContainerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows containers to be edited or deleted.
    """
    queryset = KubernetesContainer.objects.all()
    serializer_class = KubernetesContainerSerializer
    permission_classes = [permissions.IsAuthenticated]



class KubernetesPodTemplateViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows pod templates to be edited or deleted.
    """
    queryset = KubernetesPodTemplate.objects.all()
    serializer_class = KubernetesPodTemplateSerializer
    permission_classes = [permissions.IsAuthenticated]



class KubernetesDeploymentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows deployments to be edited or deleted.
    """
    queryset = KubernetesDeployment.objects.all()
    serializer_class = KubernetesDeploymentSerializer
    permission_classes = [permissions.IsAuthenticated]



class KubernetesServiceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows services to be edited or deleted.
    """
    queryset = KubernetesService.objects.all()
    serializer_class = KubernetesServiceSerializer
    permission_classes = [permissions.IsAuthenticated]



class KubernetesIngressViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows ingress to be edited or deleted.
    """
    queryset = KubernetesIngress.objects.all()
    serializer_class = KubernetesIngressSerializer
    permission_classes = [permissions.IsAuthenticated]



class KubernetesJobViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows jobs to be edited or deleted.
    """
    queryset = KubernetesJob.objects.all()
    serializer_class = KubernetesJobSerializer
    permission_classes = [permissions.IsAuthenticated]
