from django.db import models
from django.forms import CharField

# Create your models here.

class Dealership(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
