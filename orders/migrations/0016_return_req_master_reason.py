# Generated by Django 3.2 on 2022-06-05 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0015_order_master_total_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='return_req_master',
            name='REASON',
            field=models.TextField(blank=True, null=True),
        ),
    ]
