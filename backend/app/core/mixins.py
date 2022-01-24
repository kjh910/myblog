from django.db import models
from django.utils import timezone


class SoftDeleteQuerySet(models.QuerySet):
    def delete(self):
        self.update(is_deleted=True, deleted_at=timezone.now())

class SoftDeleteAllManager(models.Manager):
    """
    Custom manager to access all records.
    """
    def get_queryset(self):
        return SoftDeleteQuerySet(self.model, using=self._db)

    
class SoftDeleteDefaultManager(SoftDeleteAllManager):
    """
    By default we don't include soft-deleted records.
    """
    def get_queryset(self):
        return super(SoftDeleteDefaultManager, self).get_queryset().filter(
            is_deleted=False)


class SoftDeleteMixin(models.Model):
    class Meta:
        abstract = True

    is_deleted = models.BooleanField(
        default=False,
        help_text="Mark an item deleted without actually deleting it from database. I.e, soft deletion.")
    deleted_at = models.DateTimeField(
        blank=True, null=True,
        help_text="Soft deletion date and time."
    )

    objects = SoftDeleteDefaultManager()
    all_objects = SoftDeleteAllManager()

    def delete(self, *args, **kwargs):
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save()