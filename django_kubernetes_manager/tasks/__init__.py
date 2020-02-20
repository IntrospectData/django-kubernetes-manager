from .status import retrieve_status, status_poller
from .initialize import job_initializer_poller, initiate_job
from .cleanup import cleanup_poller, cleanup_job
from celery.schedules import crontab


def setup_periodic_tasks(sender, **kwargs):
    """Set up periodic tasks for k8s job management"""
    sender.add_periodic_task(30.0, job_initializer_poller.s(), name="K8s Job - Poll for new jobs")
    sender.add_periodic_task(60.0, status_poller.s(), name="K8s Job - Poll for status updates on running jobs")
    sender.add_periodic_task(300.0, cleanup_poller.s(), name="K8s Job - Poll for k8s job cleanup tasks")
    # Executes every Monday morning at 7:30 a.m.
    # sender.add_periodic_task(
    #     crontab(hour=7, minute=30, day_of_week=1),
    #     test.s('Happy Mondays!'),
    # )
