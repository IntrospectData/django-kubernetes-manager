from django.db import models
from solo.models import SingletonModel

# from .plan import Plan


class AppConfig(SingletonModel):
    def __str__(self):
        return "App Configuration"

    class Meta:
        verbose_name = "App Configuration"
