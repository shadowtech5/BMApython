# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-03-18 07:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('selfservice', '0007_anchorstateprice'),
    ]

    operations = [
        migrations.AddField(
            model_name='anchorbooking',
            name='unique_id',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
