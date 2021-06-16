from django.db import models
from django.contrib.auth.models import User


class Item(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField()
    description = models.TextField()

    def __str__(self):
        return self.name


class OrderCart(models.Model):
    items = models.ForeignKey(Item, on_delete=models.CASCADE)
    client = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"OrderCart's {self.client}"
    