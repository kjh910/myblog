from django.contrib import admin
from .models import Categories, Contents

@admin.register(Categories)
class Categories(admin.ModelAdmin):
    list_display = ['name',]
    search_fields = ['name',]
    readonly_fields = ['created','updated','is_deleted','deleted_at']
    
@admin.register(Contents)
class Contents(admin.ModelAdmin):
    list_display = ['content',]
    search_fields = ['content',]
    readonly_fields = ['created','updated','is_deleted','deleted_at']
# Register your models here.
