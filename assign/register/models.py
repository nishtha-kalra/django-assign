from __future__ import unicode_literals

from django.db import models

class Details(models.Model):
    name = models.CharField(max_length=200)
    password = models.CharField(max_length=100)
# Create your models here.
