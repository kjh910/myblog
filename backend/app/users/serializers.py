from rest_framework import serializers
from .models import User

class CustomUserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
         model = User
         fields = (
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
            "superhost",
         )

class CustomUserRegisterSerializer(serializers.ModelSerializer):

    class Meta:
         model = User
         fields = (
            "id",
            "email",
            "first_name",
            "last_name",
            "superhost",
         )
    
    def save(self, request,*args, **kwargs):
        user = User(
            email = self.validated_data['email'],
            username=self.validated_data['email'],
            first_name=self.validated_data['first_name'],
            last_name=self.validated_data['last_name'],
            superhost=self.validated_data['superhost'],
        )
        
        password = self.validated_data['password']
        user.set_password(password)
        user.save()
        return user