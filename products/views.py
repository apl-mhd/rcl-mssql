from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from .models import PRODUCT_MASTER
from . serializers import ProductSerializer
from rest_framework.response import Response


@api_view(['GET', 'POST'])
def product(request):
    products = PRODUCT_MASTER.objects.all()
    serializer = ProductSerializer(products, many = True)
    return Response(serializer.data)

