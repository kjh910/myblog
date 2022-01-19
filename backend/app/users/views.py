from django.shortcuts import render
from .models import User

from rest_framework import viewsets
from .serializers import CustomUserDetailsSerializer, CustomUserRegisterSerializer
from rest_framework.permissions import IsAuthenticated


# Create your views here.
      
class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = CustomUserRegisterSerializer
    permission_classes = [IsAuthenticated]
    
