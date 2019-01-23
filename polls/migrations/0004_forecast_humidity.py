# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-12-20 19:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_forecast_city'),
    ]

    operations = [
        migrations.AddField(
            model_name='forecast',
            name='humidity',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=12),
        ),
    ]