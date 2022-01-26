from django.db import models

from core import models as core_models
from core import mixins as core_mixins

# Create your models here.
class Categories(core_models.TimeStampedModel,core_mixins.SoftDeleteMixin):
    
    class Meta:
        verbose_name_plural = "Categories"
        
    name = models.CharField(
        "category_name", max_length=30, blank=True, default=""
    )
    
class Contents(core_models.TimeStampedModel,core_mixins.SoftDeleteMixin):
    
    class Meta:
        verbose_name_plural = "Contents"
        
    category = models.ForeignKey(
        Categories, related_name="category", on_delete=models.PROTECT
    )
    content = models.CharField(
        "content", max_length=5000, blank=True, default=""
    )