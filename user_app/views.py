from cgi import print_arguments
import json
from urllib import response
from django.http import HttpResponse
from django.shortcuts import render
from requests import request
from .models import  UserAccount
from . serializers import UserAccountSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login as loginuser, logout as logoutuser
from django.http import JsonResponse
from rest_framework.exceptions import AuthenticationFailed
import jwt, datetime
from rest_framework.views import APIView
from rest_framework.views import APIView

@api_view(['GET'])
def user_info(request, session_key):
    if request.method == 'GET':
         token = session_key
         if not token:
             raise AuthenticationFailed('Unauthenticated')
         try:
             payload = jwt.decode(token, 'secret', algorithms='HS256')
         except:
             raise AuthenticationFailed('token does not matched')
         user = UserAccount.objects.filter(USER_ID=payload['id']).first()
         print(user)

         serializer = UserAccountSerializer(user)
         return Response(serializer.data)
         return Response('serializer.data')
    #return HttpResponse('session_key')
    

@csrf_exempt
@api_view(['GET', 'POST'])
def LoginView(request):

    if request.method == 'POST':
        json_data =  json.loads(request.body)
        #print(json.loads(request.body.LOGIN_NAME))
        #print(len(json_data))
        login_name = json_data['LOGIN_NAME']
        swap_card = json_data['SWAP_CARD']

        user = UserAccount.objects.filter(LOGIN_NAME=login_name).first()
        
        if user is None:
            raise AuthenticationFailed('User not found')
        
        if user.SWAP_CARD != swap_card:
            raise AuthenticationFailed('incorrect password')
        
        payload = {
            'id': user.USER_ID,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }

        token = jwt.encode(payload, 'secret', algorithm='HS256') #.decode()
        response = Response()
        response.set_cookie(key='jwt', value=token, httponly=True)

        response.data = {
            'jwt': token
        }
        return response
        



def user_account(request):
    user_account = UserAccount.objects.all()
    print(user_account[0].USER_NAME)
    
    return HttpResponse('helllo')




# @api_view(['GET', 'POST'])
# def user(request):
#     users = User.objects.all()
#     print(users)
#     serializer = UserSerializer(users, many=True)
#     return Response(serializer.data)
    
            
@csrf_exempt
def logout(request):
    if request.method == 'POST':
        logoutuser(request)
        return JsonResponse({"logout":"logut"})




    