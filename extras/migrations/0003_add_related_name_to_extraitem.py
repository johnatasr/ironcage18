# Generated by Django 2.0.3 on 2018-09-06 20:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('extras', '0002_dinnerticket'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extraitem',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='extras', to=settings.AUTH_USER_MODEL),
        ),
    ]