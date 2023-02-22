from rest_framework import serializers

from .models import *


class productserializer(serializers.ModelSerializer):
    class Meta:
        model=productMainModel
        fields="__all__"
     
class productImageserializer(serializers.ModelSerializer):
    class Meta:
        model=productImageModel
        fields="__all__"
        