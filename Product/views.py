from django.shortcuts import render
from rest_framework import status, viewsets
# Create your views here.
from .serializer import *
# Create your views here.

class createProductViewSet(viewsets.ModelViewSet):
    serializer_class=productserializer
    queryset=productMainModel.objects.all()
    http_method_names=['post','get']
    


class createProductImageViewSet(viewsets.ModelViewSet):
    serializer_class=productImageserializer
    queryset=productImageModel.objects.all()
    http_method_names=['post','get']
    
    