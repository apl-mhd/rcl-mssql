from cgi import print_arguments
import json
from urllib import response
from django.http import HttpResponse
from django.shortcuts import render
from requests import request
from .models import  UserAccount, JOB_TITLES
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

#@api_view(['GET'])
def user_info(request, session_key):
    if request.method == 'GET':
         token = session_key
         if not token:
             raise AuthenticationFailed('Unauthenticated')
         try:
             payload = jwt.decode(token, 'secret', algorithms='HS256')
         except:
             raise AuthenticationFailed('token does not matched')
         user = UserAccount.objects.get(USER_ID=payload['id'])
         job_title = JOB_TITLES.objects.get(JOB_TITLE_ID=user.JOB_TITLE_ID)
         print(job_title.JOB_TITLE_NAME)

         user_json = {}
         user_json['USER_ID'] = user.USER_ID
         user_json['USER_NAME'] = user.USER_NAME
         user_json['LOGIN_NAME'] = user.LOGIN_NAME
         user_json['PASSWORD'] = user.PASSWORD
         user_json['SWAP_CARD'] = user.SWAP_CARD
         user_json['ACCESS_LEVEL'] = user.ACCESS_LEVEL
         #user_json['REG_DATE'] = user.REG_DATE
         user_json['STATUS'] = user.STATUS
         user_json['CREATED_BY'] = user.CREATED_BY
         user_json['JOB_TITLE_ID'] = job_title.JOB_TITLE_NAME
         

         user_json = json.dumps(user_json)
         return HttpResponse(user_json)

         #return Response(serializer.data)
         

    

@csrf_exempt
@api_view(['GET', 'POST'])
def LoginView(request):
    if request.method == 'POST':
        json_data =  json.loads(request.body)
        #print(json.loads(request.body.LOGIN_NAME))
        #print(len(json_data))
        login_name = json_data['username']
        swap_card = json_data['password']
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
        


@csrf_exempt
@api_view(['GET', 'POST'])
def user_account(request):
    users = UserAccount.objects.all()
    serializer = UserAccountSerializer(users, many=True)
    return Response(serializer.data)    




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




    