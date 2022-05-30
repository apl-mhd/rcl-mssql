from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from .models import Customer_Detail
from . serializers import CustomerSerializer
from rest_framework.response import Response



@api_view(['GET', 'POST'])
def customer(request):
    if request.user.is_authenticated:
        if request.user.admin:
            products = Customer_Detail.objects.all()
            serializer = CustomerSerializer(products, many = True)
            return Response(serializer.data)
        else:
            return Response('Not Authorisized')
    else:
        return Response('Not loged in')
    
@api_view(['GET', 'POST'])
def customer_register(request):

    if request.method == 'POST':
        serialzier = CustomerSerializer(data=request.data)
        if serialzier.is_valid():
            serialzier.save()
            return Response(serialzier.data)
        return Response(serialzier.errors)
        
    
    return Response('Data not inserted')



