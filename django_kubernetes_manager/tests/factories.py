import os

import factory
import factory.fuzzy
from factory.django import DjangoModelFactory as DMF
from faker import Faker

fake = Faker()

models_path = 'django_kubernetes_manager.'

microk8s_config = os.getenv('MICROK8S_CF', None)



class TargetClusterFactory(DMF):
    class Meta:
        model = models_path + 'TargetCluster'

    title = factory.fuzzy.FuzzyText(length=8, suffix="-cluster")
    description = fake.sentence()
    api_endpoint = 'https://127.0.0.1:16443'
    telemetry_endpoint = 'https://127.0.0.1:16443'
    telemetry_source = 'p'
    config = microk8s_config



class KubernetesConfigMapFactory(DMF):
    class Meta:
        model = models_path + 'KubernetesConfigMap'

    name = factory.fuzzy.FuzzyText(length=8, suffix="-cm")
    description = fake.sentence()
    cluster = factory.SubFactory(TargetClusterFactory)
    config = {"data_is_fake": "true"}
    deployed = None
    deleted = None
    kind = "ConfigMap"
    data = {"data": factory.FuzzyText(length=12)}
    namespace = "test"



class KubernetesVolumeFactory(DMF):
    class Meta:
        model = models_path + 'KubernetesVolume'

    name = factory.fuzzy.FuzzyText(length=8, suffix="-vol")
    description = fake.sentence()
    cluster = factory.SubFactory(TargetClusterFactory)
    config = {"data_is_fake": "true"}
    deployed = None
    deleted = None



class KubernetesVolumeMountFactory(DMF):
    class Meta:
        model = models_path + 'KubernetesVolumeMount'

    name = factory.fuzzy.FuzzyText(length=8, suffix="-mount")
    description = fake.sentence()
    cluster = factory.SubFactory(TargetClusterFactory)
    config = {"data_is_fake": "true"}
    deployed = None
    deleted = None
    mount_path = "/media"
    sub_path = None


class KubernetesNamespaceFactory(DMF):
    class Meta:
        model = models_path + 'KubernetesNamespace'

    name = factory.fuzzy.FuzzyText(length=8, suffix="-ns")
    description = fake.paragraph(nb_sentences=3, variable_nb_sentences=True)
    cluster = factory.SubFactory(TargetClusterFactory)
    config = {"data_is_fake": "true"}
    deployed = None
    deleted = None
    labels = {"app": fake.word()}
    annotations = None
    api_version = "v1"
    kind = "Namespace"
    exists = False



class KubernetesContainerFactory(DMF):
    class Meta:
        model = models_path + 'KubernetesContainer'

    name = factory.fuzzy.FuzzyText(length=8, suffix="-container")
    description = fake.sentence()
    cluster = factory.SubFactory(TargetClusterFactory)
    config = {"data_is_fake": "true"}
    deployed = None
    deleted = None
    image_name = factory.fuzzy.FuzzyChoice(["debian", "alpine", "busybox"])
    image_tag = "latest"
    image_pull_policy = "IfNotPresent"
    command = "/bin/sh"
    args = "-c,echo SUCCESS"
    port = factory.fuzzy.FuzzyChoice([80, 8080, 8000])
    volume_mount = None



class KubernetesPodTemplateFactory(DMF):
    class Meta:
        model = models_path + 'KubernetesPodTemplate'

    name = factory.fuzzy.FuzzyText(length=8, suffix="-pod")
    description = fake.paragraph(nb_sentences=3, variable_nb_sentences=True)
    cluster = factory.SubFactory(TargetClusterFactory)
    config = {"data_is_fake": "true"}
    deployed = None
    deleted = None
    labels = {"app": fake.word()}
    annotations = None
    volume = None
    primary_container = factory.SubFactory(KubernetesContainerFactory)
    secondary_container = None
    restart_policy = 'Always'



class KubernetesDeploymentFactory(DMF):
    class Meta:
        model = models_path + 'KubernetesDeployment'

    name = factory.fuzzy.FuzzyText(length=8, suffix="-dep")
    description = fake.paragraph(nb_sentences=3, variable_nb_sentences=True)
    cluster = factory.SubFactory(TargetClusterFactory)
    config = {"data_is_fake": "true"}
    deployed = None
    deleted = None
    labels = {"app": fake.word()}
    annotations = None
    api_version = 'apps/v1'
    kind = 'Deployment'
    port = factory.fuzzy.FuzzyChoice([80, 8080, 8000])
    namespace = 'test'
    kuid = None
    selector = labels
    replicas = 1
    pod_template = factory.SubFactory(KubernetesPodTemplateFactory)



class KubernetesJobFactory(DMF):
    class Meta:
        model = models_path + 'KubernetesJob'

    name = factory.fuzzy.FuzzyText(length=8, suffix="-job")
    description = fake.paragraph(nb_sentences=3, variable_nb_sentences=True)
    cluster = factory.SubFactory(TargetClusterFactory)
    config = {"data_is_fake": "true"}
    deployed = None
    deleted = None
    labels = {"app": fake.word()}
    annotations = None
    api_version = 'apps/v1'
    kind = 'Deployment'
    port = factory.fuzzy.FuzzyChoice([80, 8080, 8000])
    namespace = 'test'
    kuid = None
    pod_template = factory.SubFactory(KubernetesPodTemplateFactory)
    backoff_limit = factory.fuzzy.FuzzyInteger(1, 10)
