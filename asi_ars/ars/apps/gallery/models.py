from django.db import models
from django.contrib.auth.models import AbstractUser

class Image(models.Model):
    name = models.CharField(max_length=30)
    suggested = models.CharField(max_length=30, blank=True, null= True)
    image = models.CharField(max_length=120)
    retrain = models.IntegerField(blank=True, null= True)
    clase = models.CharField(max_length=1000, blank=True, null= True)
    score = models.IntegerField(blank=True, null= True)

class Time(models.Model):
    name = models.CharField(max_length=30)
    day=models.CharField(max_length=1000, blank=True, null= True)
    date=models.CharField(max_length=1000, blank=True, null= True)
    datetime=models.CharField(max_length=1000, blank=True, null= True)
    Timein=models.CharField(max_length=1000, blank=True, null= True)
    Timeout=models.CharField(max_length=1000, blank=True, null= True)


