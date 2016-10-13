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


class Location(NameMixin, models.Model):
    name = models.CharField(max_length=1024)
    latitude = models.IntegerField()
    longitude = models.IntegerField()
    users = models.ManyToManyField(User)


class Profile(models.Model):
    user = models.OneToOneField(User)
    extra = models.TextField(default='',blank=True,null=True)
    def __str__(self):
        return self.user.username


class Photo(NameMixin, models.Model):
    name = models.FileField()


class Participant(NameMixin, models.Model):
    name = models.CharField(max_length=1024,blank=True,null=True)
    weight = models.IntegerField(blank=True,null=True)
    height = models.IntegerField(blank=True,null=True)
    age = models.IntegerField(blank=True,null=True)
    notes = models.CharField(max_length=1024,blank=True,null=True)
    photo = models.ForeignKey(Photo, null=True, blank=True)
    location = models.ForeignKey(Location, null=True, blank=True)


class FeedingRecord(models.Model):
    weight = models.IntegerField(null=True, blank=True)
    date_time = models.DateField()
    participant = models.ForeignKey(Participant)
    location = models.ForeignKey(Location)
    photo = models.ForeignKey(Photo, null=True, blank=True)
    def __str__(self):
        return "{} at {}".format(self.weight, self.date_time)
