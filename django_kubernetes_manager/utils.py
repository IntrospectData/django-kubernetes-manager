import hashlib
import json
import logging
import subprocess as sp
from datetime import datetime

import yaml

from kubernetes import client, config
import re

def get_dict_hash(data):
    return hashlib.md5(json.dumps({k: data[k] for k in sorted(data.keys())}).encode("utf-8")).hexdigest()

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
