import time

from k8s_job.models.log_entry import LogEntry
from k8s_job.utils import find_namespaced_pods, log
from kubernetes import client
from kubernetes.client.rest import ApiException

from .base import CONFIG_MAP_FILE_NAME, CONFIG_MAP_KEY_NAME, CONFIG_MAP_MOUNT_PATH_BASE, CONFIG_MAP_VOLUME_NAME, K8sBase


class K8sJob(K8sBase):
    def __init__(self, *args, **kwargs):
        self.config_map = kwargs.pop("config_map", None)
        super().__init__(*args, **kwargs)

    def build_k8s_container(self):
        """Generate the k8s container object for creation in a given Kubernetes cluster"""
        container_kwargs = {}
        for k in ["image", "image_pull_policy"]:
            v = self.get_config_value("container", k, getattr(self.job_instance, k, getattr(self.job_instance.job_definition, k, None)))
            if v:
                container_kwargs[k] = v
        for k in ["args", "command"]:
            v = self.get_config_value("container", k, getattr(self.job_instance, k, getattr(self.job_instance.job_definition, k, "")))
            if v.strip():
                container_kwargs[k] = v.split(" ")

        if self.job_instance.config_map.build():
            container_kwargs["volume_mounts"] = [client.V1VolumeMount(mount_path=CONFIG_MAP_MOUNT_PATH_BASE, name=CONFIG_MAP_VOLUME_NAME)]

        return client.V1Container(name=self.job_instance.job_definition.slug, **container_kwargs)

    def build_k8s_template(self, container=None, containers=[]):
        """Given a container or list of containers, return a k8s template for use in deploying to a target cluster

            Args:
                container (V1Container) - single container spec for use in generating a PodTemplateSpec
                containers (list(V1Container)) - list of container specs for use in generating a PodTemplateSpec
            Return:
                V1PodTemplateSpec
        """
        if not container and not containers:
            raise RuntimeError("Error creating k8s template - one of [container, containers] must be specified.")
        elif not containers and container:
            containers = [container]
        elif containers and container and container not in containers:
            containers.append(container)
        podspec_kwargs = {}
        if self.job_instance.config_map.build():
            podspec_kwargs["volumes"] = [
                client.V1Volume(
                    name=CONFIG_MAP_VOLUME_NAME,
                    config_map=client.V1ConfigMapVolumeSource(
                        name=CONFIG_MAP_VOLUME_NAME,
                        items=[
                            client.V1KeyToPath(
                                key=CONFIG_MAP_KEY_NAME,
                                # mode=0777,
                                path=CONFIG_MAP_FILE_NAME,
                            )
                        ],
                    ),
                )
            ]

        return client.V1PodTemplateSpec(
            metadata=self._get_common_object_meta(),
            spec=client.V1PodSpec(restart_policy=self.get_config_value("pod", "restart_policy", "Never"), containers=containers, **podspec_kwargs),
        )

    def build_k8s_job_spec(self, template):
        """Scaffold a kubernetes JobSpec for use in creating a job in the target k8s cluster

            Args:
                template (V1PodTemplateSpec) - Pod template spec for creation of a kubernetes job
            Returns:
                V1JobSpec
        """
        job_spec_kwargs = {}
        for k in ["active_deadline_seconds", "backoff_limit", "completions", "ttl_seconds_after_finished"]:
            v = self.get_config_value("job_spec", k, getattr(self, k, None), int)
            if v:
                job_spec_kwargs[k] = v
        return client.V1JobSpec(template=template, **job_spec_kwargs)

    def build_k8s_job(self, job_spec):
        """Scaffold a kubernetes Job for use in creating a job in the target k8s cluster

            Args:
                job_spec (V1JobSpec) - Job Spec to use in creation of the kubernetes job
            Returns:
                V1Job
        """
        return client.V1Job(
            api_version=self.get_config_value("job", "api_version", "batch/v1"),
            kind=self.get_config_value("job", "kind", "Job"),
            spec=job_spec,
            metadata=self._get_common_object_meta(),
        )

    def build(self):
        """Creates the Kuberenetes-specific object for deployment"""
        container = self.build_k8s_container()
        template = self.build_k8s_template(container=container)
        spec = self.build_k8s_job_spec(template=template)
        job = self.build_k8s_job(spec)
        return job

    def create(self):
        """Create job in target K8s cluster"""
        ret_val = None
        if not self.job_instance.config_map.read() and self.job_instance.config_map.build():
            self.job_instance.config_map.create()
        with self.job_instance.get_k8s_client(API=client.BatchV1Api) as api_client:
            ret_val = api_client.create_namespaced_job(body=self.build(), namespace=self.job_instance.namespace)
        return ret_val

    def read(self):
        """Read details of job from K8s"""
        ret_val = None
        try:
            with self.job_instance.get_k8s_client(API=client.BatchV1Api) as api_client:
                ret_val = api_client.read_namespaced_job(name=str(self.job_instance.id), namespace=self.job_instance.namespace)
        except ApiException as e:
            log.warning("API Exception attempting to read {} - {}".format(self.job_instance.id, e))
        return ret_val

    def delete(self, wait=True, wait_sec=20):
        """Deletes job from K8s cluster"""
        ret_val = False
        log.debug("delete_job - read first: {}".format(self.read()))
        if self.read():
            with self.job_instance.get_k8s_client(API=client.BatchV1Api) as api_client:
                api_response = api_client.delete_namespaced_job(name=str(self.job_instance.id), namespace=self.job_instance.namespace)
                log.debug("delete_job - api_response: {}".format(api_response))
            if api_response:
                if self.job_instance.config_map.read():
                    self.job_instance.config_map.delete()
                while not ret_val and wait and wait_sec > 0:
                    read_status = self.read()
                    if read_status:
                        wait_sec += -2
                        log.debug("Waiting 2 sec - {} sec to go for delete on {}".format(wait_sec, str(self.job_instance.id)))
                        time.sleep(2)
                    else:
                        ret_val = True
            else:
                ret_val = True
        return ret_val

    def get_job_logs(self):
        """Gets job logs from pods found for the job deployed"""
        ret_val = []
        with self.job_instance.get_k8s_client(API=client.CoreV1Api) as api_client:
            for pod_name in find_namespaced_pods(self.job_instance.namespace, str(self.job_instance.id), api_client):
                log.debug("Found pod {} in namespace {}".format(pod_name, self.job_instance.namespace))
                for entry in api_client.read_namespaced_pod_log(pod_name, self.job_instance.namespace, timestamps=True).split("\n"):
                    ret_val.append(entry)
                    LogEntry.add(job_instance=self.job_instance, message=entry, source="p", pod_id=pod_name)
        return ret_val
