# Generated by Django 3.2 on 2022-06-04 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_product_master_table'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product_master',
            name='id',
        ),
        migrations.AlterField(
            model_name='product_master',
            name='PROD_CODE_SL',
            field=models.BigIntegerField(primary_key=True, serialize=False),
        ),
    ]