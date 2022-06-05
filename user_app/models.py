from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser
from django.utils import timezone
from django.utils.translation import gettext_lazy as _  
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import BaseUserManager

class JOB_TITLES(models.Model):
    JOB_TITLE_ID = models.BigIntegerField(primary_key=True)
    JOB_TITLE_NAME = models.TextField()
    class Meta:
        db_table = 'JOB_TITLES'

class UserAccount(models.Model):
    USER_ID = models.BigIntegerField(primary_key=True)
    USER_NAME = models.CharField(max_length=50)
    LOGIN_NAME = models.CharField(max_length=50)
    PASSWORD = models.TextField()
    SWAP_CARD = models.CharField(max_length=50)
    ACCESS_LEVEL = models.CharField(max_length=50)
    REG_DATE = models.DateTimeField(auto_now_add=True)
    STATUS = models.CharField(max_length=50)
    CREATED_BY = models.BigIntegerField()
    JOB_TITLE_ID = models.BigIntegerField()
    

    class Meta:
        db_table = 'USER_ACCOUNT'







