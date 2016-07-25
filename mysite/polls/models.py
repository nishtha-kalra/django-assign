from __future__ import unicode_literals

from django.db import models

# Create your models here.


class register(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    password = models.CharField(max_length=100)
    re_password = models.CharField(max_length=100)


class directory(models.Model):
    dir_name = models.CharField(max_length=50)
    phone_number = models.PositiveIntegerField(max_length=10)
    address = models.CharField(max_length=300)
    alt_number = models.PositiveIntegerField(max_length=10)

