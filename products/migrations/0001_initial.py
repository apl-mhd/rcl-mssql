# Generated by Django 3.2 on 2022-05-29 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PRODUCT_MASTER',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PROD_CODE_SL', models.BigIntegerField(blank=True, null=True)),
                ('PROD_CODE', models.BigIntegerField(blank=True, null=True)),
                ('PROD_DESC', models.TextField(blank=True, null=True)),
                ('BARCODE', models.CharField(blank=True, max_length=50, null=True)),
                ('GROUP_CODE', models.CharField(blank=True, max_length=10, null=True)),
                ('SUPPLIER_CODE', models.BigIntegerField(blank=True, null=True)),
                ('BRAND', models.CharField(blank=True, max_length=50, null=True)),
                ('MANUFACTURER_CODE', models.BigIntegerField(blank=True, null=True)),
                ('PRODUCT_SIZE', models.CharField(blank=True, max_length=50, null=True)),
                ('UNIT', models.CharField(blank=True, max_length=50, null=True)),
                ('MEASURE_TYPE', models.CharField(blank=True, max_length=50, null=True)),
                ('AVERAGE_COST', models.FloatField(blank=True, null=True)),
                ('STANDARD_COST', models.FloatField(blank=True, null=True)),
                ('SALES_RATE', models.FloatField(blank=True, null=True)),
                ('TAXCODE', models.CharField(blank=True, max_length=20, null=True)),
                ('MAX_STOCK', models.IntegerField(blank=True, null=True)),
                ('MIN_STOCK', models.IntegerField(blank=True, null=True)),
                ('USER_ID', models.BigIntegerField(blank=True, null=True)),
                ('WARRANTY_DURATION', models.BigIntegerField(blank=True, null=True)),
                ('INVENTORY_FLAG', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]