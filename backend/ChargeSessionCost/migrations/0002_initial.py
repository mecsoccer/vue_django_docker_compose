# Generated by Django 4.1.7 on 2023-02-21 13:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ChargeSessionCost', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='chargesessioncost',
            name='user_info',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]