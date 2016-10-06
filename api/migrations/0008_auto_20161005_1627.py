# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-05 16:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20161005_1620'),
    ]

    operations = [
        migrations.AlterField(
            model_name='day',
            name='date_time',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='feedingrecord',
            name='photo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Photo'),
        ),
        migrations.AlterField(
            model_name='feedingrecord',
            name='weight',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]