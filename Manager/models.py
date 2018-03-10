# coding=utf8
from django.db import models


# Create your models here.
class Products(models.Model):
    name = models.CharField(max_length=1000)
    productType = models.CharField(max_length=100)
    produceTime = models.DateField(null=True)
    picture = models.ImageField(upload_to="goods_image/")
    expTime = models.IntegerField(null=True)
    price = models.FloatField()
    info = models.CharField(max_length=1000)
    saleTime = models.DateField()
    Inventory = models.IntegerField()