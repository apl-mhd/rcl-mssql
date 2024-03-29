from django.db import models


class PRODUCT_MASTER(models.Model):
    PROD_CODE_SL = models.BigIntegerField(primary_key=True)
    PROD_CODE = models.BigIntegerField(blank=True, null=True)
    PROD_DESC = models.TextField( blank=True, null=True)
    BARCODE = models.CharField(max_length=50, blank=True, null=True)
    GROUP_CODE = models.CharField(max_length=10, blank=True, null=True)
    SUPPLIER_CODE = models.BigIntegerField(blank=True, null=True)
    BRAND = models.CharField(max_length=50, blank=True, null=True)
    MANUFACTURER_CODE = models.BigIntegerField(blank=True, null=True)
    PRODUCT_SIZE = models.CharField(max_length=50, blank=True, null=True)
    COLOUR = models.CharField(max_length=50, blank=True, null=True)
    MEASURE_TYPE = models.CharField(max_length=50, blank=True, null=True)
    AVERAGE_COST = models.FloatField(blank=True, null=True)
    STANDARD_COST = models.FloatField(blank=True, null=True)
    SALES_RATE = models.FloatField(blank=True, null=True)
    TAXCODE = models.CharField(max_length=20, blank=True, null=True)
    MAX_STOCK =models.IntegerField(blank=True, null=True)
    MIN_STOCK =models.IntegerField(blank=True, null=True)
    USER_ID =models.BigIntegerField(blank=True, null=True)
    WARRANTY_DURATION =models.BigIntegerField(blank=True, null=True)
    INVENTORY_FLAG =models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'PRODUCT_MASTER'



class PRODUCT_MASTER_1(models.Model):
    PROD_CODE_SL = models.BigIntegerField(primary_key=True)
    PROD_CODE = models.BigIntegerField()
    PROD_DESC = models.TextField( blank=True, null=True)
    BARCODE = models.CharField(max_length=50, blank=True, null=True)
    GROUP_CODE = models.CharField(max_length=10, blank=True, null=True)
    PRODUCT_LINE_CODE =  models.TextField( blank=True, null=True)
    SUPPLIER_CODE = models.BigIntegerField(blank=True, null=True)
    BRAND = models.CharField(max_length=50, blank=True, null=True)
    MANUFACTURER_CODE = models.BigIntegerField(blank=True, null=True)
    PRODUCT_SIZE = models.CharField(max_length=50, blank=True, null=True)
    UNIT = models.CharField(max_length=50, blank=True, null=True)
    MEASURE_TYPE = models.CharField(max_length=50, blank=True, null=True)
    AVERAGE_COST = models.FloatField(blank=True, null=True)
    STANDARD_COST = models.FloatField(blank=True, null=True)
    LAST_COST = models.FloatField(blank=True, null=True)
    SALES_RATE = models.FloatField(blank=True, null=True)
    TAXCODE = models.CharField(max_length=20, blank=True, null=True)
    DISCOUNT_CODE = models.BigIntegerField(blank=True, null=True)
    MAX_STOCK =models.IntegerField(blank=True, null=True)
    MIN_STOCK =models.IntegerField(blank=True, null=True)
    PRODUCT_IMAGE = models.BinaryField(blank = True, null=True)
    USER_ID = models.BigIntegerField(blank=True, null=True)
    STATUS  = models.CharField(max_length=50, blank=True, null=True)
    WARRANTY_DURATION = models.BigIntegerField(blank=True, null=True)
    WARRANTY_DURATION_TYPE = models.CharField(max_length=15, blank=True, null=True)
    INVENTORY_FLAG =models.IntegerField(blank=True, null=True)

    #COLOUR = models.CharField(max_length=50, blank=True, null=True)
    

    class Meta:
        db_table = 'PRODUCT_MASTER_1'


