# Generated by Django 3.2 on 2022-06-04 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_customer_detail_contact_person'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer_detail',
            name='CUSTOMER_ID',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
