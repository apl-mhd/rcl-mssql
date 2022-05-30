# Generated by Django 3.2 on 2022-05-27 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email address')),
                ('is_active', models.BooleanField(default=True)),
                ('staff', models.BooleanField(default=False)),
                ('admin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Customer_Detail',
            fields=[
                ('CUSTOMER_ID', models.AutoField(primary_key=True, serialize=False)),
                ('CUSTOMER_NAME', models.CharField(blank=True, max_length=50, null=True)),
                ('CONTACT_PERSON', models.CharField(blank=True, max_length=50, null=True)),
                ('PRESENT_ADDRESS', models.TextField(blank=True, null=True)),
                ('TEL', models.CharField(blank=True, max_length=50, null=True)),
                ('MOB', models.CharField(blank=True, max_length=50, null=True)),
                ('EMAIL', models.CharField(blank=True, max_length=50, null=True)),
                ('DOT', models.CharField(blank=True, max_length=50, null=True)),
                ('CUSTOMER_PIC', models.ImageField(blank=True, null=True, upload_to='')),
                ('USER_ID', models.BigIntegerField(blank=True, null=True)),
                ('ZONE_CODE', models.CharField(blank=True, max_length=50, null=True)),
                ('RECEIVABLE_ACCOUNT_CODE', models.BigIntegerField(blank=True, null=True)),
                ('CLIENT_LEVEL', models.CharField(blank=True, max_length=25, null=True)),
                ('STATUS', models.CharField(blank=True, max_length=15, null=True)),
                ('REP_CODE', models.BigIntegerField(blank=True, null=True)),
                ('CUST_CAT', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]
