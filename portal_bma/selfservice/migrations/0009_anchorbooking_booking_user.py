# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-03-18 08:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('selfservice', '0008_anchorbooking_unique_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='anchorbooking',
            name='booking_user',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
