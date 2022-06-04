# Generated by Django 3.2 on 2022-06-02 10:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ORDER_MASTER',
            fields=[
                ('DOT', models.DateTimeField(auto_now_add=True, null=True)),
                ('ORDER_NO', models.BigIntegerField(primary_key=True, serialize=False, unique=True)),
                ('CUSTOMER_ID', models.IntegerField(blank=True, null=True)),
                ('LATITUDE', models.DecimalField(blank=True, decimal_places=6, max_digits=18, null=True)),
                ('LOGITUDE', models.DecimalField(blank=True, decimal_places=6, max_digits=18, null=True)),
                ('USER_ID', models.BigIntegerField(blank=True, null=True)),
                ('STATUS', models.CharField(default='PENDING', max_length=25)),
                ('ORDERDETAILS', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'ORDER_MASTER',
            },
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ORDER_DETAILS',
            fields=[
                ('ORDER_TRANSAC_SL', models.AutoField(primary_key=True, serialize=False)),
                ('ORDER_NO', models.BigIntegerField(blank=True, null=True)),
                ('RATE', models.IntegerField(blank=True, null=True)),
                ('QTY', models.DecimalField(decimal_places=4, max_digits=18)),
                ('ITEM_PRICE', models.DecimalField(decimal_places=4, max_digits=18)),
                ('PROD_CODE', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.product_master')),
            ],
        ),
    ]
