
from dataclasses import fields
from rest_framework import serializers
from . models import PRODUCT_MASTER

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = PRODUCT_MASTER
        fields = '__all__'
        #fields = '__all__' 



