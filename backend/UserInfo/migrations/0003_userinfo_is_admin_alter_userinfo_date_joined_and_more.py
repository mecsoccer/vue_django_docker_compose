# Generated by Django 4.1.7 on 2023-02-21 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserInfo', '0002_userinfo_date_joined_userinfo_is_active_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='is_admin',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='date_joined',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='email',
            field=models.EmailField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='first_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='is_superuser',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='last_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='password',
            field=models.CharField(max_length=128, verbose_name='password'),
        ),
    ]
