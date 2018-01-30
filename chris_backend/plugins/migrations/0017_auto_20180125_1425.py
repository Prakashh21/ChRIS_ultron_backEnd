# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2018-01-25 19:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plugins', '0016_auto_20171018_1242'),
    ]

    operations = [
        migrations.AddField(
            model_name='plugin',
            name='authors',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='plugin',
            name='category',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='plugin',
            name='description',
            field=models.CharField(blank=True, max_length=800),
        ),
        migrations.AddField(
            model_name='plugin',
            name='documentation',
            field=models.CharField(blank=True, max_length=800),
        ),
        migrations.AddField(
            model_name='plugin',
            name='license',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='plugin',
            name='title',
            field=models.CharField(blank=True, max_length=400),
        ),
        migrations.AddField(
            model_name='plugin',
            name='version',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]