import logging

from celery import shared_task
from kubernetes import client, config

log = logging.getLogger(__name__)
config.load_kube_config()

def create_deployment(apps_v1_api, **kwargs):
    kwargs = kwargs.get("kwargs")
    kwargs["binary_path"]="https://storage.googleapis.com/id-public-read/model.h5" #<-- for local testing
    #volume definition
    volume = client.V1Volume(
        name="{}-vol".format(kwargs.get('k8s_name')),
        empty_dir={}
    )
    #volumeMount definition
    volume_mount = client.V1VolumeMount(
        name="{}-vol".format(kwargs.get('k8s_name')),
        mount_path="/media"
    )
    #container definition
    container = client.V1Container(
        name=kwargs.get('k8s_name'),
        image=kwargs.get('k8s_image'),
        image_pull_policy="Always",
        ports=[client.V1ContainerPort(container_port=kwargs.get('k8s_ctr_port'))],
        volume_mounts = [volume_mount]
    )
    #sidecar definition
    sidecar = client.V1Container(
        name="{}-curl".format(kwargs.get('k8s_name')),
        image="curlimages/curl",
        image_pull_policy="IfNotPresent",
        volume_mounts = [volume_mount],
        command=["/bin/sh","-c"],
        args=["curl {} -o /media/{}; curl {}/api/ready; exit".format(
            kwargs.get("binary_path"),
            kwargs.get("binary_path").split("/")[-1],
            "http://" + kwargs.get("host") + ":" + str(kwargs.get("k8s_ctr_port"))
        )],
        ports=[client.V1ContainerPort(container_port=9000)],
    )
    #pod definition
    template = client.V1PodTemplateSpec(
        metadata=client.V1ObjectMeta(
            labels={"app": kwargs.get('k8s_name')},
            annotations={
                "prometheus.io/scrape": "true",
                "prometheus.io/path": "/metrics",
                "prometheus.io/port": str(kwargs.get('k8s_ctr_port', 8080))
            }
        ),
        spec=client.V1PodSpec(
            volumes=[volume],
            containers=[container, sidecar]
        )
    )
    #deployment spec
    spec = client.V1DeploymentSpec(
        selector={'matchLabels': {"app": kwargs.get('k8s_name')}},
        replicas=1,
        template=template)
    #deployment definition
    deployment = client.V1Deployment(
        api_version="apps/v1",
        kind="Deployment",
        metadata=client.V1ObjectMeta(
            name=kwargs.get('k8s_name'),
            labels={"app": kwargs.get('k8s_name')}
        ),
        spec=spec)
    # Creation of the Deployment in specified namespace
    # (Can replace "default" with a namespace you may have created)
    apps_v1_api.create_namespaced_deployment(
        namespace=kwargs.get('k8s_namespace'), body=deployment
    )
    return True

def create_service(kwargs):
    kwargs = kwargs.get("kwargs")
    core_v1_api = client.CoreV1Api()
    body = client.V1Service(
        api_version="v1",
        kind="Service",
        metadata=client.V1ObjectMeta(
            name="{}-svc".format(kwargs.get('k8s_name'))
        ),
        spec=client.V1ServiceSpec(
            selector={"app": kwargs.get('k8s_name')},
            ports=[client.V1ServicePort(
                port=kwargs.get('k8s_svc_port'),
                target_port=kwargs.get('k8s_ctr_port')
            )]
        )
    )
    # Creation of the Deployment in specified namespace
    # (Can replace "default" with a namespace you may have created)
    core_v1_api.create_namespaced_service(namespace=kwargs.get('k8s_namespace'), body=body)
    return True

def create_ingress(networking_v1_beta1_api, **kwargs):
    kwargs = kwargs.get("kwargs")
    print(kwargs)
    body = client.NetworkingV1beta1Ingress(
        api_version="networking.k8s.io/v1beta1",
        kind="Ingress",
        metadata=client.V1ObjectMeta(name="{}-ing".format(kwargs.get('k8s_name')), annotations={
            "nginx.ingress.kubernetes.io/rewrite-target": "/"
        }),
        spec=client.NetworkingV1beta1IngressSpec(
            rules=[client.NetworkingV1beta1IngressRule(
                host=kwargs.get('host'),
                http=client.NetworkingV1beta1HTTPIngressRuleValue(
                    paths=[client.NetworkingV1beta1HTTPIngressPath(
                        path="/",
                        backend=client.NetworkingV1beta1IngressBackend(
                            service_port=kwargs.get('k8s_svc_port'),
                            service_name="{}-svc".format(kwargs.get('k8s_name')))

                    )]
                )
            )
            ]
        )
    )
    # Creation of the Deployment in specified namespace
    # (Can replace "default" with a namespace you may have created)
    networking_v1_beta1_api.create_namespaced_ingress(
        namespace=kwargs.get('k8s_namespace'),
        body=body
    )
    return True
