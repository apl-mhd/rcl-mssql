# Generated by Django 3.2 on 2022-05-29 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0002_auto_20220529_1539'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='status',
            field=models.BooleanField(default=True, verbose_name='status'),
        ),
    ]