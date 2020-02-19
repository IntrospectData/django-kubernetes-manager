from celery import shared_task
from celery.utils.log import get_task_logger
from k8s_job.models import JobInstance

log = get_task_logger(__name__)


@shared_task(bind=True)
def initiate_job(self, job_instance_id):
    """Celery task to create k8s resources for a given JobInstance

        Args:
            job_instance_id (str) - primary key for the JobInstance being initiated
        Return:
            dict
    """
    job_instance = JobInstance.objects.get(pk=job_instance_id)
    return job_instance.job.create()


@shared_task(bind=True)
def job_initializer_poller(self):
    """Celery task to take all uninitialized tasks and dispatch them to be created in their target k8s cluster"""
    tasks = []
    for job in JobInstance.objects.filter(state="New").all():
        tasks.append(initiate_job.apply_async(kwargs={"job_instance_id": str(job.id)}).id)
        job.mark_initialized()
        job.save()
    return tasks
