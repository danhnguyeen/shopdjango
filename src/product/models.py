from django.db import models

class Category(models.Model):
  title = models.CharField(max_length=255)
  slug = models.CharField(max_length=100)
  description = models.TextField(null=True, blank=True)
  active = models.BooleanField(default=True)


class Product(models.Model):
  name = models.CharField(max_length=255)
  description = models.TextField(null=True, blank=True)
  category = models.ForeignKey(Category, on_delete=models.CASCADE)
  price = models.FloatField(default=0)
  active = models.BooleanField(default=True)


class Variation(models.Model):
  product = models.ForeignKey(Product, on_delete=models.CASCADE)
  title = models.CharField(max_length=255)
  price = models.FloatField(default=0)
  sale_price = models.FloatField(default=0)
  inventory = models.IntegerField(default=0)
  active = models.BooleanField(default=True)
  
