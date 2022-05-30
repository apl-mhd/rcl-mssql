
from dataclasses import fields
from rest_framework import serializers
from . models import *

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = PRODUCT_MASTER
        fields = '__all__'
        #fields = '__all__' 



