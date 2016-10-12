from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_profile(sender, instance=None, created=False, **kwargs):
    if created:
        Profile.objects.create(user=instance)


class NameMixin(object):
    def __str__(self):
        return self.name


class Team(NameMixin, models.Model):
    name = models.CharField(max_length=1024)


class Profile(models.Model):
    user = models.OneToOneField(User)
    team = models.ForeignKey(Team, null=True, blank=True)
    
    def __str__(self):
        return self.user.username


class FeedingProgram(NameMixin, models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=1024)
    country = models.CharField(max_length=1024)


class Location(NameMixin, models.Model):
    name = models.CharField(max_length=1024)
    latitude = models.IntegerField()
    longitude = models.IntegerField()
    feeding_program = models.ForeignKey(FeedingProgram)


class Photo(models.Model):
    image = models.FileField()
    def __str__(self):
        return str(self.image)


class Kid(models.Model):
    height = models.IntegerField(blank=True,null=True)
    first_name = models.CharField(max_length=1024,blank=True,null=True)
    last_name = models.CharField(max_length=1024,blank=True,null=True)
    notes = models.CharField(max_length=1024,blank=True,null=True)
    weight = models.IntegerField(blank=True,null=True)
    age = models.IntegerField(blank=True,null=True)

    def __str__(self):
        return self.first_name


class FeedingRecord(models.Model):
    weight = models.IntegerField(null=True, blank=True)
    date_time = models.DateField()
    kid = models.ForeignKey(Kid)
    location = models.ForeignKey(Location)
    photo = models.ForeignKey(Photo, null=True, blank=True)



