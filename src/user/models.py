from django.db import models
from django.contrib.auth.models import AbstractUser


class Customer(AbstractUser):
  phone = models.CharField(max_length=15, blank=True, null=True)
  address = models.CharField(max_length=255, blank=True, null=True)
