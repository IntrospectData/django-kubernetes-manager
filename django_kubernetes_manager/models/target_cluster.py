import hashlib
import json
from tempfile import NamedTemporaryFile

import yaml

from django.contrib.postgres.fields import JSONField
from django.db import models
from django_extensions.db.models import TitleSlugDescriptionModel

from ..utils import log, split_kubeconfig

QUERY_TEMPLATE = "{}://{}/api/v1/query?query={}"
RANGE_TEMPLATE = "{}://{}/api/v1/query_range?query={}&start={}&end={}&step={}"

TELEMETRY_SOURCE = (("p", "Prometheus"),)


class TargetCluster(TitleSlugDescriptionModel):

    api_endpoint = models.URLField(help_text="Cluster Endpoint URL")
    telemetry_endpoint = models.URLField(help_text="Telemetry Endpoint URL")
    telemetry_source = models.CharField(max_length=5, default="p", choices=TELEMETRY_SOURCE)
    config = JSONField(help_text="Configuration data stored as an encrypted blob in the database", null=True)

    @classmethod
    def add(cls, kubeconfig):
        """Class method to a new TargetCluster

            Args:
                kubeconfig (str) - string contents of kubeconfig file
            Returns:
                list(TargetCluster)
        """
        if not isinstance(kubeconfig, bytes):
            kubeconfig = kubeconfig.encode("utf-8")
        config_hash_str = hashlib.md5().hexdigest()[:8]
        config_data = yaml.load(kubeconfig, Loader=yaml.FullLoader)
        ret_val = []
        for item in config_data.get("clusters", []):
            cluster, created = TargetCluster.objects.get_or_create(title=item.get("name"), api_endpoint=item.get("cluster", {}).get("server"))
            if created:
                ret_val.append(cluster)
                cluster.config = str(json.dumps(config_data))
                cluster.save()
        for config_obj in split_kubeconfig(kubeconfig):
            cluster, created = TargetCluster.objects.get_or_create(
                title=config_obj.get("clusters", [])[0].get("name"), api_endpoint=config_obj.get("clusters", [])[0].get("cluster", {}).get("server")
            )
            ret_val.append(cluster)
            if created:
                cluster.config = config_data
                cluster.save()
                log.info("Created new cluster record for {} @ {}".format(cluster.title, cluster.api_endpoint))
            else:
                log.warning("Cluster record for {} @ {} already existed - TargetCluster not added".format(cluster.title, cluster.api_endpoint))
        if ret_val:
            log.info("Added {} clusters".format(len(ret_val)))
        else:
            log.warning("No clusters added")
        return ret_val
