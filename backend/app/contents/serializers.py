from .models import Categories, Contents
from rest_framework import serializers

class CategoriesSerializers(serializers.ModelSerializer):
    
    class Meta:
         model = Categories
         fields = (
            "id",
            "name",
            "is_deleted",
         )

class ContentsSerializers(serializers.ModelSerializer):
    
    class Meta:
         model = Contents
         fields = (
            "id",
            "content",
            "is_deleted",
         )