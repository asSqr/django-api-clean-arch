from django.db import models
from django.contrib.auth.models import User


class Item(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField()
    description = models.TextField()


class OrderCart(models.Model):
    items = models.ForeignKey(Item, on_delete=models.CASCADE)
    client = models.OneToOneField(User, on_delete=models.CASCADE)
