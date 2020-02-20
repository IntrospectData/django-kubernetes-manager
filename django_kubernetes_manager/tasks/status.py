from celery import shared_task
from celery.utils.log import get_task_logger
from k8s_job.models import JobInstance
from ..utils import read_job_status, read_pod_usage
log = get_task_logger(__name__)


@shared_task(bind=True)
def retrieve_status(self, job_instance_id):
    job = JobInstance.objects.get(job_instance_id)
    return read_job_status(job_name=job.name, job_namespace=job.namespace)

@shared_task(bind=True)
def retrieve_usage(self, job_instance_id):
    job = JobInstance.objects.get(job_instance_id)
    return read_job_status(pod_name=job.name, pod_namespace=job.namespace)

@shared_task(bind=True)
def status_poller(self):
    tasks = []
    for job in JobInstance.objects.filter(is_complete=False).filter(is_complete=False).all():
        tasks.append(retrieve_status.apply_async(kwargs={"job_instance_id": str(job.id)}).id)
    return tasks
