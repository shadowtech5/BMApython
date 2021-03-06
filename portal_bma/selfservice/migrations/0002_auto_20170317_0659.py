# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-03-17 06:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('selfservice', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='anchortravel',
            name='preffered_place',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='preffered_place',
            field=models.CharField(blank=True, choices=[('KERALA', 'KERALA'), ('NATIONAL', 'NATIONAL'), ('INTERNATIONAL', 'INTERNATIONAL')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='star_rating',
            field=models.CharField(blank=True, choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], max_length=10, null=True),
        ),
    ]
