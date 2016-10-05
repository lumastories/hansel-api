from django.contrib.auth.models import User
from django.contrib.postgres.fields import JSONField
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User)
    extra = JSONField()


class FeedingProgram(models.Model):
    team = models.ManyToManyField(User)
    name = models.CharField(max_length=1024)
    country = models.CharField(max_length=1024)


class Location(models.Model):
    name = models.CharField(max_length=1024)
    latitude = models.IntegerField()
    longitude = models.IntegerField()
    feeding_program = models.ForeignKey(FeedingProgram)


class Photo(models.Model):
    image = models.FileField()
    

class Day(models.Model):
    date_time = models.DateField()


class Kid(models.Model):
    height = models.IntegerField()
    first_name = models.CharField(max_length=1024)
    last_name = models.CharField(max_length=1024)
    notes = models.CharField(max_length=1024)
    weight = models.IntegerField()
    age = models.IntegerField()


class FeedingRecord(models.Model):
    weight = models.IntegerField()
    date_time = models.DateField()
    day = models.ForeignKey(Day)
    kid = models.ForeignKey(Kid)
    location = models.ForeignKey(Location)
    photo = models.ForeignKey(Photo)



