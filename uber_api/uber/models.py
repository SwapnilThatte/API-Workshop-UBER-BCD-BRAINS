from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class User(models.Model):
    name = models.CharField( max_length=50)
    email = models.EmailField(max_length=254)
    number = models.PhoneNumberField()
    password = models.CharField( max_length=50)

class Driver(models.Model):
    name = models.CharField( max_length=50)
    email = models.EmailField(max_length=254)
    car_no = models.CharField(max_length=50)
    number = models.PhoneNumberField()
    upload = models.ImageField(upload_to = user_directory_path)
    rating = models.CharField( max_length=50)

class Ride(models.Model):
    price = models.CharField( max_length=50)
    current_loc = models.EmailField(max_length=254)
    destination = models.CharField(max_length=50)
    pickup = models.TimeField(auto_now=False, auto_now_add=False)
    
class UsrHistory(models.Model):
    startLoc = models.CharField(max_length=50)
    review = models.CharField( max_length=50)
    dest = models.CharField(max_length=50)
    last_rides = models.DateField(auto_now=False, auto_now_add=False)
