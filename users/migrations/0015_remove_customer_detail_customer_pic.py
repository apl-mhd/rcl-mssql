# Generated by Django 3.2 on 2022-06-05 09:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0014_alter_customer_detail_customer_pic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer_detail',
            name='CUSTOMER_PIC',
        ),
    ]
