import hashlib
import json
import logging
import subprocess as sp
from datetime import datetime

import yaml

from celery import shared_task
from kubernetes import client, config
import re

def get_dict_hash(data):
    return hashlib.md5(json.dumps({k: data[k] for k in sorted(data.keys())}).encode("utf-8")).hexdigest()


log = logging.getLogger(__name__)
config.load_kube_config()

byte_units = {
    "E": 1000**6, "P": 1000**5, "T": 1000**4,
    "G": 1000**3, "M": 1000**2, "K": 1000,
    "Ei": 1024**6, "Pi": 1024**5, "Ti": 1024**4,
    "Gi": 1024**3, "Mi": 1024**2, "Ki": 1024
}

def splitNumeric(size):
    return filter(None, re.split(r'(\d+)', size))

def parseSize(size):
    number, unit = [string for string in splitNumeric(size)]
    return int(float(number)*byte_units[unit])


def create_job_obj(job_name="default-job", job_image="debian", job_port=80, job_args="sleep 120", host="localhost" ):
    #volume definition
    volume = client.V1Volume(
        name="{}-vol".format(job_name),
        empty_dir={}
    )
    #volumeMount definition
    volume_mount = client.V1VolumeMount(
        name="{}-vol".format(job_name),
        mount_path="/media"
    )
    #container definition
    container = client.V1Container(
        name=job_name,
        image=job_image,
        image_pull_policy="Always",
        ports=[client.V1ContainerPort(container_port=job_port)],
        volume_mounts = [volume_mount],
        command=["/bin/sh"],
        args=["-c", job_args]
    )
    #pod definition
    template = client.V1PodTemplateSpec(
        metadata=client.V1ObjectMeta(
            labels={"app": job_name},
            annotations={
                "prometheus.io/scrape": "true",
                "prometheus.io/path": "/metrics",
                "prometheus.io/port": str(job_port)
            }
        ),
        spec=client.V1PodSpec(
            volumes=[volume],
            containers=[container],
            restart_policy="Never"
        )
    )
    spec = client.V1JobSpec(
        template=template,
        backoff_limit=4
    )
    job = client.V1Job(
        api_version="batch/v1",
        kind="Job",
        metadata=client.V1ObjectMeta(name=job_name),
        spec=spec
    )
    return job

def run_job(api_instance=client.BatchV1Api(), job=create_job_obj(), namespace='default'):
    api_response = api_instance.create_namespaced_job(
        body = job,
        namespace = namespace
    )
    return api_response.status

def delete_job(api_instance, job_name, job_namespace):
    api_response = api_instance.delete_namespaced_job(
        name=job_name,
        namespace=job_namespace,
        body=client.V1DeleteOptions(
            propagation_policy='Foreground',
            grace_period_seconds=5))
    return api_response.status

def read_job_status(api_instance=client.BatchV1Api(), job_name="default-job", job_namespace="default"):
    api_response = api_instance.read_namespaced_job_status(job_name, job_namespace)
    return api_response.status

def read_pod_metrics(api_instance=client.CustomObjectsApi(), pod_name="default-pod", pod_namespace="default"):
    items = api_instance.list_cluster_custom_object('metrics.k8s.io', 'v1beta1', 'pods').get("items", [])
    return [pod for pod in items if pod_name in pod.get("metadata", {}).get("name") and pod_namespace in pod.get("metadata", {}).get("namespace")]

def read_pod_usage(pod_name="default-pod", pod_namespace="default"):
    pod_metrics = read_pod_metrics(pod_name=pod_name, pod_namespace=pod_namespace)
    cpu = 0.000
    memory = 0
    for metric in pod_metrics:
        for container in metric.get("containers", []):
            ccpu = container.get("usage", {}).get("cpu", None)
            cmem = container.get("usage", {}).get("memory", None)
            if 'm' in ccpu:
                ccpu = int(ccpu.split("m")[0]) / 1000.000
            cpu += ccpu
            memory += parseSize(cmem)
    return {'cpu': cpu, 'memory': memory}

###
# okay so I guess what I need to do is make a moving average and record usage and timestamps
#    from there I can then extrapolate a metric I am calling vcpu-seconds which is pretty much Killowat hours but for pods

# def vcpuseconds():
#     for each second in time
#         store read pog usage in db
#         update mviung average
#     vcpu_seconds = avg usage * timestamp delta
#     return vcpu_seconds

def run_command(cmd, log_method=log.info):
    """Subprocess wrapper for capturing output of processes to logs
    """
    if isinstance(cmd, str):
        cmd = cmd.split(" ")
    start = datetime.utcnow()
    log_method("Starting run_command for: {}".format(" ".join([str(x) for x in cmd])))
    p = sp.Popen(cmd, bufsize=0, stdout=sp.PIPE, stderr=sp.STDOUT)
    ret_val = None
    while True:
        line = p.stdout.readline()
        ret_val = p.poll()
        if not line and ret_val != None:
            break
        log_method(line.decode())
    log_method("Completed run_command in {} for: {}".format((datetime.utcnow() - start).total_seconds(), " ".join(cmd)))
    return ret_val


def get_command_output(cmd):
    """ retrieve command output for a given command provided
    """
    if isinstance(cmd, str):
        cmd = cmd.split(" ")
    pipe = sp.Popen(cmd, stdout=sp.PIPE, stderr=sp.STDOUT)
    out, err = pipe.communicate()
    return out


def find_namespaced_pods(namespace, job_name, api_client):
    """find pod by namespace and job name

        Args:
            namespace (str) -
            job_name (str) -
            api_client (CoreV1Api) -
        Returns:
            str - Name of the pod if found
    """
    api_response = api_client.list_namespaced_pod(namespace)
    ret_val = []
    for i in api_response.items:
        if i.metadata.labels.get("job_instance_id", "") == job_name:
            ret_val.append(i.metadata.name)
    return ret_val


def generate_kubeconfig(context, cluster, user, default_name="k8s-job-runner"):
    """Format helper for generating individual cluster kubeconfigs

        Args:
            context (dict) -
            cluster (dict) -
            user (dict) -
        Returns:
            dict -
    """
    if "name" not in context:
        context["name"] = default_name
    for input in [context, cluster, user]:
        while not isinstance(input, dict) and isinstance(input, list):
            cluster = cluster[0]
    return {
        "apiVersion": "v1",
        "kind": "Config",
        "preferences": {},
        "clusters": [cluster],
        "users": [user],
        "contexts": [context],
        "current-context": context.get("name"),
    }


def split_kubeconfig(kubeconfig):
    """Helper method to split a kubeconfig into separate, per-cluster configurations

        Args:
            kubeconfig (dict or str) -
        Returns:
            list(dict)
    """
    if not isinstance(kubeconfig, dict):
        kubeconfig = yaml.load(kubeconfig, Loader=yaml.FullLoader)
    ret_val = []
    for context in kubeconfig.get("contexts", []):
        cluster = [x for x in kubeconfig.get("clusters", []) if x.get("name") == context.get("context", {}).get("cluster", "")][0]
        user = [x for x in kubeconfig.get("users", []) if x.get("name") == context.get("context", {}).get("user", "")][0]
        if cluster and user:
            ret_val.append(generate_kubeconfig(context, cluster, user))
    return ret_val


def coalesce_dicts(target={}, source={}):
    if source:
        if isinstance(source, bytes):
            source = source.decode("utf-8")
        if isinstance(source, str):
            source = json.loads(source)
        target.update(source)
    return target
