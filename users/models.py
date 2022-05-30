from django.db import models
from django.contrib.auth.models import AbstractBaseUser, AbstractUser
from django.utils import timezone


# class CustomUser(AbstractUser):
#     address = models.CharField(max_length=30, blank=True, null=True)
#     date_joined = models.DateTimeField(default=timezone.now)  
#     birth_date = models.DateField
#     is_staff = models.BooleanField(default=True)
#     is_active = models.BooleanField(default=True)
#     is_superuser = models.BooleanField(default=True)


class Customer_Detail(models.Model):
    CUSTOMER_ID = models.AutoField(primary_key=True)
    CUSTOMER_NAME = models.CharField(max_length=50, blank=True, null=True)
    CONTACT_PERSON = models.CharField(max_length=50, blank=True, null=True)
    PRESENT_ADDRESS = models.TextField(blank=True, null=True)
    TEL = models.CharField(max_length=50, blank=True, null=True)
    MOB = models.CharField(max_length=50, blank=True, null=True)
    EMAIL = models.CharField(max_length=50, blank=True, null=True)
    DOT = models.CharField(max_length=50, blank=True, null=True)
    CUSTOMER_PIC = models.ImageField(blank=True, null=True)
    USER_ID = models.BigIntegerField(blank=True, null=True)
    ZONE_CODE = models.CharField(max_length=50, blank=True, null=True)
    RECEIVABLE_ACCOUNT_CODE = models.BigIntegerField( blank=True, null=True)
    CLIENT_LEVEL = models.CharField(max_length=25, blank=True, null=True)
    STATUS = models.CharField(max_length=15, blank=True, null=True)
    REP_CODE = models.BigIntegerField( blank=True, null=True)
    CUST_CAT = models.CharField(max_length=50, blank=True, null=True)
    

    def __str__(self):
        return self.CUSTOMER_NAME
    
   