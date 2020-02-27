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



class KubernetesContainerFactory(DMF):
    class Meta:
        model = models_path + 'KubernetesContainer'

    name = factory.fuzzy.FuzzyText(length=8, suffix="-container")
    description = fake.sentence()
    cluster = factory.SubFactory(TargetClusterFactory)
    config = fake.pydict()
    deployed = None
    deleted = None
    image_name = factory.fuzzy.FuzzyChoice(["debian", "alpine", "busybox"])
    image_tag = "latest"
    image_pull_policy = "IfNotPresent"
    command = "/bin/sh"
    args = "-c,sleep 6000"
    port = factory.fuzzy.FuzzyChoice([80, 8080, 8000])
    volume_mount = None



class KubernetesPodTemplateFactory(DMF):
    class Meta:
        model = models_path + 'KubernetesPodTemplate'

    name = factory.fuzzy.FuzzyText(length=8, suffix="-container")
    description = fake.paragraph(nb_sentences=3, variable_nb_sentences=True)
    cluster = factory.SubFactory(TargetClusterFactory)
    config = fake.pydict(nb_elements=4, variable_nb_elements=True)
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

    name = factory.fuzzy.FuzzyText(length=8, suffix="-container")
    description = fake.paragraph(nb_sentences=3, variable_nb_sentences=True)
    cluster = factory.SubFactory(TargetClusterFactory)
    config = fake.pydict(nb_elements=4, variable_nb_elements=True)
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

    name = factory.fuzzy.FuzzyText(length=8, suffix="-container")
    description = fake.paragraph(nb_sentences=3, variable_nb_sentences=True)
    cluster = factory.SubFactory(TargetClusterFactory)
    config = fake.pydict(nb_elements=4, variable_nb_elements=True)
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
