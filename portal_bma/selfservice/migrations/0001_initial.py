# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-03-17 06:31
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AnchorActive',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(blank=True, max_length=50, null=True)),
                ('time', models.CharField(blank=True, max_length=50, null=True)),
                ('available', models.CharField(choices=[('ONLINE', 'ONLINE'), ('OFFLINE', 'OFFLINE'), ('BUSY', 'BUSY')], max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AnchorLanguage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(choices=[('ENGLISH', 'ENGLISH'), ('MALAYALAM', 'MALAYALAM'), ('TAMIL', 'TAMIL'), ('KANNADA', 'KANNADA'), ('PUNJABI', 'PUNJABI'), ('TELUGU', 'TELUGU'), ('MARATHI', 'MARATHI')], max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AnchorTravel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('travel', models.CharField(choices=[('KERALA', 'KERALA'), ('NATIONAL', 'NATIONAL'), ('INTERNATIONAL', 'INTERNATIONAL')], max_length=50)),
                ('preffered_place', models.CharField(choices=[('KERALA', 'KERALA'), ('NATIONAL', 'NATIONAL'), ('INTERNATIONAL', 'INTERNATIONAL')], max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='EventTypes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_type', models.CharField(choices=[('SHOW', 'SHOW'), ('CAMPUS', 'CAMPUS'), ('KIDS PARTY', 'KIDS PARTY'), ('PRIVATE PARTY', 'PRIVATE PARTY'), ('INAUGURATION', 'INAUGURATION'), ('CORPRATE', 'CORPRATE'), ('PROMOTIONS', 'PROMOTIONS'), ('EXIBITIONS', 'EXIBITIONS'), ('FASHION SHOW', 'FASHION SHOW'), ('WEDDING', 'WEDDING')], max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_celebrity', models.BooleanField(default=False)),
                ('is_anchor', models.BooleanField(default=False)),
                ('bma_code', models.CharField(blank=True, max_length=15, null=True)),
                ('gender', models.CharField(choices=[('MALE', 'MALE'), ('FEMALE', 'FEMALE')], max_length=50)),
                ('place', models.CharField(blank=True, max_length=50, null=True)),
                ('mobile_number', models.CharField(blank=True, max_length=10, null=True)),
                ('biography', models.TextField(null=True)),
                ('star_rating', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], max_length=10)),
                ('charge', models.CharField(blank=True, max_length=10, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
