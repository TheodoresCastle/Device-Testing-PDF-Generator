# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-08-10 19:45
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_forms', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='completetest',
            name='inspection_date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='completetest',
            name='inspection_time',
            field=models.TimeField(default=datetime.time),
        ),
    ]