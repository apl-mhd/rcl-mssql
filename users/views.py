from functools import partial
import re
from urllib import response
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from .models import Customer_Detail
from . serializers import CustomerSerializer
from rest_framework.response import Response
from django.core.files.storage import FileSystemStorage


@api_view(['GET', 'POST'])
def customer_update(request, id):
    if request.method == 'POST':
        customer = Customer_Detail.objects.get(CUSTOMER_ID=id)
        serializer = CustomerSerializer(customer, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    return Response('get')


@api_view(['GET', 'POST'])
def customer(request):

    if request.method == 'POST':
        request.data._mutable=True #if submit from data, for json it woud be false
        # upload = request.FILES['img']
        # fss = FileSystemStorage()
        # file = fss.save(upload.name, upload)
        # print(fss.url(file))
        #request.data['CUST_CAT'] = fss.url(file)

        customer_detail = Customer_Detail.objects.all().last()
        request.data['CUSTOMER_ID'] = customer_detail.CUSTOMER_ID +1
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    if request.method == 'GET':
        customers = Customer_Detail.objects.all()
        serializer = CustomerSerializer(customers, many = True)
        return Response(serializer.data)
       
    
@api_view(['GET', 'POST'])
def customer_register(request):
    if request.method == 'POST':
        serialzier = CustomerSerializer(data=request.data)
        if serialzier.is_valid():
            serialzier.save()
            return Response(serialzier.data)
        return Response(serialzier.errors)  
    return Response('Data not inserted')



