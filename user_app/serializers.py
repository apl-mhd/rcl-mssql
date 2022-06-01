from dataclasses import fields
from rest_framework import serializers
from .models import User, UserAccount


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model =  User
        fields = '__all__'

class UserAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = '__all__'