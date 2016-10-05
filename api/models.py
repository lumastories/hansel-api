from django.db import models

class Kid(models.Model):
    height = models.IntegerField()
    first_name = models.CharField(max_length=1024)
    last_name = models.CharField(max_length=1024)
    notes = models.CharField(max_length=1024)
    weight = models.IntegerField()
    age = models.IntegerField()

