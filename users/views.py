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
        #print(type(request.data), '----------')  #class 'dict'(json),  for form data django.http.request.QueryDict'
        #if type(request.data) == 'django.http.request.QueryDict':
        request.data._mutable=True

        # upload = request.FILES['img']
        # fss = FileSystemStorage()
        # file = fss.save(upload.name, upload)
        # print(fss.url(file))

        customer_detail = Customer_Detail.objects.all().last()
        request.data['CUSTOMER_ID'] = customer_detail.CUSTOMER_ID +1
        a = request.FILES['CUSTOMER_PIC'].file.read()
        b= Customer_Detail.objects.create(
           CUSTOMER_ID =  customer_detail.CUSTOMER_ID +1,
           CUSTOMER_PIC = a,
        )

        print(b)
        
        # request.data['CUSTOMER_PIC'] = a
        # serializer = CustomerSerializer(data=request.data)
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data)
        # else:
        #     return Response(serializer.errors)
        return Response('a')

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



