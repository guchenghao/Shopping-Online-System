from django.db import models

# Create your models here.
class shoppingCart(models.Model):
    cusID = models.IntegerField()
    productID = models.IntegerField()
    quantity = models.IntegerField()


class orderList(models.Model):
    cusID = models.IntegerField()
    orderTime = models.DateField()
    address = models.CharField(max_length=100)
    totalPrice = models.FloatField()
    orderState = models.CharField(max_length=30)

    class Meta:
        ordering = ['-id']


class orderDetail(models.Model):
    orderID = models.IntegerField()
    productID = models.IntegerField()
    productName = models.CharField(max_length=500)
    pic_url = models.CharField(max_length=100)
    username = models.CharField(max_length=10)
    quantity = models.IntegerField()
    buyPrice = models.FloatField()