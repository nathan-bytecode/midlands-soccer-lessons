from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Account(models.Model):
    name = models.CharField(max_length=200, unique=True)
    email = models.EmailField(max_length=200, unique=True)
    phone = models.IntegerField(unique=True)
    photo = models.ImageField(unique=True)
    author = models.ForeignKey(
    User, on_delete=models.CASCADE, related_name="account"
)

# Course 1 model for boys aged 7+
class Course1(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    price = models.IntegerField()

    def __str__(self):
        return self.title

# Course 2 model for boys aged 14+
class Course2(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    price = models.IntegerField()

    def __str__(self):
        return self.title

# Course 3 model for girls aged 9+
class Course3(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    price = models.IntegerField()

    def __str__(self):
        return self.title