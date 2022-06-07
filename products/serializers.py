
from dataclasses import fields
from rest_framework import serializers
from . models import PRODUCT_MASTER, PRODUCT_MASTER_1

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = PRODUCT_MASTER
        fields = '__all__'
        #fields = '__all__' 

class ProductOneSerializer(serializers.ModelSerializer):
    class Meta:
        model = PRODUCT_MASTER_1
        fields = '__all__'



