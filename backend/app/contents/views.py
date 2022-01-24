from .models import Categories, Contents
from rest_framework import viewsets
from .serializers import CategoriesSerializers, ContentsSerializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

# Create your views here.
class CategoriesViewSet(viewsets.ModelViewSet):
    queryset=Categories.objects.all()
    serializer_class = CategoriesSerializers
    permission_classes = [IsAuthenticated]

class ContentsViewSet(viewsets.ModelViewSet):
    queryset=Contents.objects.all()
    serializer_class = ContentsSerializers
    permission_classes = [IsAuthenticated]