# Generated by Django 3.2 on 2022-06-04 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_alter_customer_detail_customer_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer_detail',
            name='PRESENT_ADDRESS',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='customer_detail',
            name='CUSTOMER_ID',
            field=models.BigIntegerField(primary_key=True, serialize=False),
        ),
    ]
