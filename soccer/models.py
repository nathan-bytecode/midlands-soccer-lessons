from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Account(models.Model):
    name = models.CharField(max_length=200, unique=True)
    email = models.EmailField(max_length=200, unique=True)
    phone = models.IntegerField(unique=True)
    photo = models.ImageField(unique=True)
    author = models.ForeignKey(
    User, on_delete=models.CASCADE, related_name="account"
)