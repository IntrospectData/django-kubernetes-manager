from celery import shared_task
from celery.utils.log import get_task_logger
from k8s_job.models import JobInstance

log = get_task_logger(__name__)


@shared_task(bind=True)
def cleanup_job(self, job_instance_id):
    ret_val = False
    j = JobInstance.objects.get(pk=job_instance_id)
    if not j.timestamps.get("cleanup"):
        j.cleanup()
        j.save()
        ret_val = j.timestamps.get("cleanup")
    return ret_val


@shared_task(bind=True)
def cleanup_poller(self):
    pass
