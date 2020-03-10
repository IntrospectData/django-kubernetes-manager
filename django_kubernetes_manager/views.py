from rest_framework import permissions, viewsets
from rest_framework.decorators import action

from .models import (KubernetesContainer, KubernetesDeployment,
                     KubernetesIngress, KubernetesJob, KubernetesPodTemplate,
                     KubernetesService, TargetCluster)
from .serializers import (KubernetesContainerSerializer,
                          KubernetesDeploymentSerializer,
                          KubernetesIngressSerializer, KubernetesJobSerializer,
                          KubernetesPodTemplateSerializer,
                          KubernetesServiceSerializer, TargetClusterSerializer)



class TargetClusterViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows cluster configs to be edited or deleted
    """
    queryset = TargetCluster.objects.all()
    serializer_class = TargetClusterSerializer
    permission_classes = [permissions.IsAuthenticated]

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

    @action(methods=['post'], detail=True)
    def deploy(self, request, *args, **kwargs):
        """
        Action to deploy the kubernetes resource to target cluster.
        """
        return KubernetesDeployment.objects.get(pk=kwargs['pk']).deploy()

    @action(methods=['post'], detail=True)
    def k_delete(self, request, *args, **kwargs):
        """
        Action to delete the kubernetes resource from the cluster/namespaces
        """
        return KubernetesDeployment.objects.get(pk=kwargs['pk']).k_delete()

    @action(methods=['post'], detail=True)
    def pod_usage(self, request, *args, **kwargs):
        """
        Action to fetch point-in-time cpu and memory usage of pod.
        """
        return KubernetesDeployment.objects.get(pk=kwargs['pk']).read_pod_usage()


class KubernetesServiceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows services to be edited or deleted.
    """
    queryset = KubernetesService.objects.all()
    serializer_class = KubernetesServiceSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(methods=['post'], detail=True)
    def deploy(self, request, *args, **kwargs):
        """
        Action to deploy the kubernetes resource to target cluster.
        """
        return KubernetesService.objects.get(pk=kwargs['pk']).deploy()

    @action(methods=['post'], detail=True)
    def k_delete(self, request, *args, **kwargs):
        """
        Action to delete the kubernetes resource from the cluster/namespace.
        """
        return KubernetesService.objects.get(pk=kwargs['pk']).k_delete()



class KubernetesIngressViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows ingress to be edited or deleted.
    """
    queryset = KubernetesIngress.objects.all()
    serializer_class = KubernetesIngressSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(methods=['post'], detail=True)
    def deploy(self, request, *args, **kwargs):
        """
        Action to deploy the kubernetes resource to target cluster.
        """
        return KubernetesIngress.objects.get(pk=kwargs['pk']).deploy()

    @action(methods=['post'], detail=True)
    def k_delete(self, request, *args, **kwargs):
        """
        Action to delete the kubernetes resource from the cluster/namespace.
        """
        return KubernetesIngress.objects.get(pk=kwargs['pk']).k_delete()



class KubernetesJobViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows jobs to be edited or deleted.
    """
    queryset = KubernetesJob.objects.all()
    serializer_class = KubernetesJobSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(methods=['post'], detail=True)
    def deploy(self, request, *args, **kwargs):
        """
        Action to deploy the kubernetes resource to target cluster.
        """
        return KubernetesJob.objects.get(pk=kwargs['pk']).deploy()

    @action(methods=['post'], detail=True)
    def k_delete(self, request, *args, **kwargs):
        """
        Action to delete the kubernetes resource from the target cluster/ns.
        """
        return KubernetesJob.objects.get(pk=kwargs['pk']).k_delete()

    @action(methods=['post'], detail=True)
    def pod_usage(self, request, *args, **kwargs):
        """
        Action to fetch point-in-time cpu and memory usage of pod.
        """
        return KubernetesJob.objects.get(pk=kwargs['pk']).read_pod_usage()
