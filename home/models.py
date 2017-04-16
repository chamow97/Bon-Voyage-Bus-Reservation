from django.db import models
from django.http import HttpResponse
from django.contrib.auth.models import Permission, User

class Bus(models.Model):
    name = models.CharField(max_length=300)
    source = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    capacity = models.IntegerField()
    fare = models.FloatField()
