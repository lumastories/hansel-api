# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-05 05:08
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0002_auto_20161005_0118'),
    ]

    operations = [
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='FeedingProgram',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1024)),
                ('country', models.CharField(max_length=1024)),
                ('team', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='FeedingRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.IntegerField()),
                ('date_time', models.DateField()),
                ('day', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Day')),
                ('kid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Kid')),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1024)),
                ('latitude', models.IntegerField()),
                ('longitude', models.IntegerField()),
                ('feeding_program', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.FeedingProgram')),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('extra', django.contrib.postgres.fields.jsonb.JSONField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='feedingrecord',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Location'),
        ),
        migrations.AddField(
            model_name='feedingrecord',
            name='photo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Photo'),
        ),
    ]