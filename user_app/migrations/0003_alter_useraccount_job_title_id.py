# Generated by Django 3.2 on 2022-06-05 12:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0002_alter_useraccount_job_title_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccount',
            name='JOB_TITLE_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_app.job_titles'),
        ),
    ]
