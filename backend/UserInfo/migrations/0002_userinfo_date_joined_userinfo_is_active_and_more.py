# Generated by Django 4.1.7 on 2023-02-21 15:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('UserInfo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='date_joined',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
    ]