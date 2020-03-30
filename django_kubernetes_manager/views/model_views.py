from rest_framework import permissions, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import (KubernetesContainer, KubernetesDeployment,
                     KubernetesIngress, KubernetesJob, KubernetesPodTemplate,
                     KubernetesService, TargetCluster, KubernetesNamespace,
                     KubernetesConfigMap)
from .serializers import (KubernetesContainerSerializer,
                          KubernetesDeploymentSerializer,
                          KubernetesIngressSerializer, KubernetesJobSerializer,
                          KubernetesPodTemplateSerializer,
                          KubernetesServiceSerializer, TargetClusterSerializer,
                          KubernetesNamespaceSerializer,
                          KubernetesConfigMapSerializer)



class TargetClusterViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows cluster configs to be edited or deleted
    """
    queryset = TargetCluster.objects.all()
    serializer_class = TargetClusterSerializer
    permission_classes = [permissions.IsAuthenticated]



class KubernetesNamespaceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows namespaces to be created or deleted
    """
    queryset = KubernetesNamespace.objects.all()
    serializer_class = KubernetesNamespaceSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(methods=['post', 'get'], detail=True)
    def deploy(self, request, *args, **kwargs):
        """
        Action to deploy the namespace resource to target cluster.
        """
        return Response(KubernetesNamespace.objects.get(pk=kwargs['pk']).deploy())

    @action(methods=['post', 'get'], detail=True)
    def k_delete(self, request, *args, **kwargs):
        """
        Action to delete the kubernetes namespace from the cluster.
        """
        return Response(KubernetesNamespace.objects.get(pk=kwargs['pk']).k_delete())



class KubernetesConfigMapViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows configmaps to be edited or deleted
    """
    queryset = KubernetesConfigMap.objects.all()
    serializer_class = KubernetesConfigMapSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(methods=['post', 'get'], detail=True)
    def deploy(self, request, *args, **kwargs):
        """
        Action to deploy the ConfigMap resource to target cluster.
        """
        return Response(KubernetesConfigMap.objects.get(pk=kwargs['pk']).deploy())

    @action(methods=['post', 'get'], detail=True)
    def k_delete(self, request, *args, **kwargs):
        """
        Action to delete the kubernetes ConfigMap from the cluster.
        """
        return Response(KubernetesConfigMap.objects.get(pk=kwargs['pk']).k_delete())



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

    @action(methods=['post', 'get'], detail=True)
    def deploy(self, request, *args, **kwargs):
        """
        Action to deploy the kubernetes resource to target cluster.
        """
        return Response(KubernetesDeployment.objects.get(pk=kwargs['pk']).deploy())

    @action(methods=['post', 'get'], detail=True)
    def k_delete(self, request, *args, **kwargs):
        """
        Action to delete the kubernetes resource from the cluster/namespaces
        """
        return Response(KubernetesDeployment.objects.get(pk=kwargs['pk']).k_delete())

    @action(methods=['post', 'get'], detail=True)
    def pod_usage(self, request, *args, **kwargs):
        """
        Action to fetch point-in-time cpu and memory usage of pod.
        """
        return Response(KubernetesDeployment.objects.get(pk=kwargs['pk']).read_pod_usage())



class KubernetesServiceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows services to be edited or deleted.
    """
    queryset = KubernetesService.objects.all()
    serializer_class = KubernetesServiceSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(methods=['post', 'get'], detail=True)
    def deploy(self, request, *args, **kwargs):
        """
        Action to deploy the kubernetes resource to target cluster.
        """
        return Response(KubernetesService.objects.get(pk=kwargs['pk']).deploy())

    @action(methods=['post', 'get'], detail=True)
    def k_delete(self, request, *args, **kwargs):
        """
        Action to delete the kubernetes resource from the cluster/namespace.
        """
        return Response(KubernetesService.objects.get(pk=kwargs['pk']).k_delete())



class KubernetesIngressViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows ingress to be edited or deleted.
    """
    queryset = KubernetesIngress.objects.all()
    serializer_class = KubernetesIngressSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(methods=['post', 'get'], detail=True)
    def deploy(self, request, *args, **kwargs):
        """
        Action to deploy the kubernetes resource to target cluster.
        """
        return Response(KubernetesIngress.objects.get(pk=kwargs['pk']).deploy())

    @action(methods=['post', 'get'], detail=True)
    def k_delete(self, request, *args, **kwargs):
        """
        Action to delete the kubernetes resource from the cluster/namespace.
        """
        return Response(KubernetesIngress.objects.get(pk=kwargs['pk']).k_delete())



class KubernetesJobViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows jobs to be edited or deleted.
    """
    queryset = KubernetesJob.objects.all()
    serializer_class = KubernetesJobSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(methods=['post', 'get'], detail=True)
    def deploy(self, request, *args, **kwargs):
        """
        Action to deploy the kubernetes resource to target cluster.
        """
        return Response(KubernetesJob.objects.get(pk=kwargs['pk']).deploy())

    @action(methods=['post', 'get'], detail=True)
    def k_delete(self, request, *args, **kwargs):
        """
        Action to delete the kubernetes resource from the target cluster/ns.
        """
        return Response(KubernetesJob.objects.get(pk=kwargs['pk']).k_delete())

    @action(methods=['post', 'get'], detail=True)
    def pod_usage(self, request, *args, **kwargs):
        """
        Action to fetch point-in-time cpu and memory usage of pod.
        """
        return Response(KubernetesJob.objects.get(pk=kwargs['pk']).read_pod_usage())
