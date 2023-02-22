from django.shortcuts import render
from rest_framework import status, viewsets

from .serializer import *
# Create your views here.

class AccountViewSet(viewsets.ModelViewSet):
    serializer_class=userserializer
    http_method_names=['post','get']
    queryset=User.objects.all()
    
    
class userProfileModel(viewsets.ModelViewSet):
    serializer_class=userProfileSerializer
    http_method_names=['post']
    queryset=userProfileModel.objects.all()