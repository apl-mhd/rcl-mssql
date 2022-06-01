from urllib import request
from django.db import models
from products.models import PRODUCT_MASTER
from users.models import Customer_Detail

class ORDER_MASTER(models.Model):
    DOT = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    ORDER_NO = models.BigIntegerField(primary_key=True, unique=True)
    CUSTOMER_ID =  models.IntegerField(blank=True, null=True)
    LATITUDE = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    LOGITUDE = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    USER_ID = models.BigIntegerField(blank=True, null=True)
    STATUS = models.CharField(max_length=25, default='PENDING')
    ORDERDETAILS = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'ORDER_MASTER'

    def __str__(self):
        return str(self.ORDER_NO)

    
class ORDER_DETAILS(models.Model):
    ORDER_TRANSAC_SL = models.AutoField(primary_key=True)
    ORDER_NO = models.BigIntegerField(blank=True, null=True)
    PROD_CODE = models.ForeignKey(PRODUCT_MASTER, on_delete=models.CASCADE, blank=True, null=True)
    RATE = models.IntegerField(blank=True, null=True)
    QTY = models.DecimalField(max_digits=18, decimal_places=4)
    ITEM_PRICE = models.DecimalField(max_digits=18, decimal_places=4)


class Test(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)





