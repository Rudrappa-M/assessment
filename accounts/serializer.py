from rest_framework import serializers
from accounts.models import *

class userserializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields="__all__"
        
        
class userProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=userProfileModel
        fields="__all__"
        