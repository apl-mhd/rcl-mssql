# Generated by Django 3.2 on 2022-05-29 10:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_delete_customuser'),
        ('orders', '0003_alter_order_master_dot'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order_master',
            name='CUSTOMER_ID',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.customer_detail'),
        ),
    ]
