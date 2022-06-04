from functools import partial
import re
from urllib import response
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from .models import Customer_Detail
from . serializers import CustomerSerializer
from rest_framework.response import Response

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
        customer_detail = Customer_Detail.objects.all().last()
        request.data['CUSTOMER_ID'] = customer_detail.CUSTOMER_ID +1
        serializer = CustomerSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        else:
            return Response(serializer.errors)
       
        # customer = Customer_Detail.objects.create(
        #     CUSTOMER_ID=customer_detail.CUSTOMER_ID +1,
        #     CUSTOMER_NAME = request.data['CUSTOMER_NAME'],
        #     CONTACT_PERSON = request.data['CONTACT_PERSON'],
        #     CUST_CAT = request.data['CUST_CAT'],
        #     STATUS = request.data['STATUS']
        #     )
        # serializer = CustomerSerializer(customer)
        # return Response(serializer.data)
       

    if request.method == 'GET':
        products = Customer_Detail.objects.all()
        serializer = CustomerSerializer(products, many = True)
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



