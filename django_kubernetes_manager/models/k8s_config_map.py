from uuid import uuid4

from k8s_job.utils import log
from kubernetes import client
from kubernetes.client.rest import ApiException

from .base import CONFIG_MAP_FILE_NAME, CONFIG_MAP_KEY_NAME, CONFIG_MAP_MOUNT_PATH_BASE, CONFIG_MAP_VOLUME_NAME, K8sBase


class K8sConfigMap(K8sBase):
    """Kubernetes ConfigMap that allows for usage of a script within a config map mounted to a container"""

    def build(self):
        """Optionally generate a for a script to be run within the container"""
        ret_val = None
        if self.job_instance.script:
            ret_val = client.V1ConfigMap(kind="ConfigMap", metadata=self._get_common_object_meta(), data={CONFIG_MAP_KEY_NAME: self.job_instance.script})
        return ret_val

    def create(self):
        """Create a config map object from this JobInstance's data"""
        if self.build():
            with self.job_instance.get_k8s_client() as api_client:
                return api_client.create_namespaced_config_map(body=self.build(), namespace=self.job_instance.namespace)
        return None

    def read(self):
        """Makes request to the target k8s cluster and returns currently deployed status/details"""
        if self.build():
            try:
                with self.job_instance.get_k8s_client() as api_client:
                    return api_client.read_namespaced_config_map(name=str(self.job_instance.id), namespace=self.job_instance.namespace)
            except ApiException as e:
                log.warning("API Exception attempting to read {} - {}".format(self.job_instance.id, e))
        return None

    def delete(self):
        """Makes request to the target k8s cluster and attempts to delete the deployed config map"""
        if self.read():
            with self.job_instance.get_k8s_client() as api_client:
                api_response = api_client.delete_namespaced_config_map(name=str(self.job_instance.id), namespace=self.job_instance.namespace)
            if api_response:
                return True
        return False
