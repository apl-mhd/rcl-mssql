from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from . models import ORDER_MASTER

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = ORDER_MASTER
        fields = '__all__'
        
