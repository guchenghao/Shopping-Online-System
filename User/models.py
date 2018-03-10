from django.db import models


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=10, unique=True)
    password = models.CharField(max_length=10)
    registration_date = models.DateField()
    telephone = models.CharField(max_length=11)
    address = models.CharField(max_length=50)
    email = models.CharField(max_length=25, null=True)


class Manager(models.Model):
    name = models.CharField(max_length=10, unique=True)
    password = models.CharField(max_length=10)