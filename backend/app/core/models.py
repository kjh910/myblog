from django.db import models
from . import managers
from django.utils import timezone


class TimeStampedModel(models.Model):

    """ Time Stamped Model """

    created = models.DateTimeField(default=timezone.now())
    updated = models.DateTimeField(default=timezone.now())
    objects = managers.CustomModelManager()

    class Meta:
        abstract = True
        