from django.db import models

from user.models import Customer
from cart.models import Cart

class Order(models.Model):
  user = models.ForeignKey(Customer, on_delete=models.CASCADE)
  cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
  shipping_address = models.CharField(max_length=255, blank=True, null=True)
  order_description = models.TextField(blank=True, null=True)
  is_completed = models.BooleanField(default=False)
  
