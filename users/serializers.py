
from dataclasses import fields
from rest_framework import serializers
from . models import *

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer_Detail
        fields = '__all__'



