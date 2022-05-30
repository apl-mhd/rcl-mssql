from cgi import print_arguments
from urllib import response
from django.http import HttpResponse
from django.shortcuts import render
from .models import User
from . serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login as loginuser, logout as logoutuser
from django.http import JsonResponse





@api_view(['GET', 'POST'])
def user(request):
    users = User.objects.all()
    print(users)
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)
    




@csrf_exempt
def login(request):
    if request.method == 'POST':
        byte_body = request.body
        body = eval(byte_body.decode('utf-8'))
        login_name = body['username']
        password = body['password']
        user = authenticate(login_name=login_name, password=password)
        if user is not None:
                request.session.set_expiry(86400)
                loginuser(request, user)
                session = {'session': request.session.session_key}
                return JsonResponse(session)
        return JsonResponse({"details":"Unauthorized"})
            
@csrf_exempt
def logout(request):
    if request.method == 'POST':
        logoutuser(request)
        return JsonResponse({"logout":"logut"})




    