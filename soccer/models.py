from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

STATUS = ((0, "Not Live"), (1, "Live"))
BOOKING_STATUS = ((0, "Awaiting Confirmation"), (1, "Confirm Booking"),
                  (2, "Booking Declined"))

class Account(models.Model):
    first_name = models.CharField(max_length=200, unique=True, default='SOME STRING')
    last_name = models.CharField(max_length=200, unique=True, default='SOME STRING')
    email = models.EmailField(max_length=200, unique=True)
    phone = models.IntegerField(unique=True)
    photo = models.ImageField(unique=True)

    def __str__(self):
        if self.user:
            return f"{self.first_name + ' ' + self.last_name}"
        else:
            return f"New Account / Not Provided"

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

# Booking model for when selecting a course
class Booking(models.Model):
    course_choice = [
        ('course1', "COURSE1 - Boys Aged 7-14 (60euros per boy)"),
        ('course2', "COURSE2 - Boys Aged 14-21 (80euros per boy)"),
        ('course2', "COURSE2 - Girls Aged 9-14 (40euros per girl)"),
    ]
    
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    course_selection = models.CharField(max_length=10, choices=course_choice)
    email = models.EmailField()
    contact_phone = models.CharField(max_length=15, null=False, blank=False)
    booking_date = models.DateField(null=False, blank=False)
    booking_time = models.CharField(null=False, blank=False, max_length=5)
    number_of_attendees = models.IntegerField(default=1, blank=False)
    booking_status = models.IntegerField(choices=BOOKING_STATUS, default=0)