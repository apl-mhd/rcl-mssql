from django.db import models
from django.contrib.auth.models import AbstractBaseUser, AbstractUser
from django.utils import timezone



class Customer_Detail(models.Model):
    CUSTOMER_ID = models.BigIntegerField(primary_key=True)
    CUSTOMER_NAME = models.CharField(max_length=50, blank=True, null=True)
    CONTACT_PERSON = models.CharField(max_length=50, blank=True, null=True)
    PRESENT_ADDRESS = models.TextField(blank=True, null=True)
    #CUSTOMER_PIC = models.ImageField(blank=True, null=True)
    USER_ID = models.BigIntegerField(blank=True, null=True)
    ZONE_CODE = models.CharField(max_length=50, blank=True, null=True)
    ADV_ACCOUNT_CODE = models.BigIntegerField( blank=True, null=True)
    RECEIVABLE_ACCOUNT_CODE = models.BigIntegerField( blank=True, null=True)
    CLIENT_LEVEL = models.CharField(max_length=25, blank=True, null=True)
    STATUS = models.CharField(max_length=15, blank=True, null=True)
    REP_CODE = models.BigIntegerField( blank=True, null=True)
    CREDIT_LIMIT = models.BigIntegerField( blank=True, null=True)
    CUST_CAT = models.CharField(max_length=50, blank=True, null=True)
    

    class Meta:
        db_table = 'CUSTOMER_DETAILS'


    

   