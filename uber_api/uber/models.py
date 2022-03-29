from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class User1(models.Model):
    name = models.TextField( default=None, unique=True)
    email = models.EmailField(max_length=254, null=True)
    number = models.IntegerField(null=True)
    password = models.CharField( max_length=50, null=True)

class Driver(models.Model):
    name = models.CharField( max_length=50)
    email = models.EmailField(max_length=254)
    car_no = models.CharField(max_length=50)
    number = models.IntegerField()
    # upload = models.ImageField(upload_to = user_directory_path)
    rating = models.CharField( max_length=50)

class Ride(models.Model):
    usr = models.ForeignKey(User1, on_delete=models.SET_NULL , null=True)
    price = models.CharField( max_length=50)
    current_loc = models.CharField(max_length=254)
    destination = models.CharField(max_length=50)
    pickup = models.TimeField(auto_now=False, auto_now_add=False)
    
class UsrHistory(models.Model):
    startLoc = models.CharField(max_length=50)
    review = models.CharField( max_length=50)
    dest = models.CharField(max_length=50)
    last_rides = models.DateField(auto_now=False, auto_now_add=False)
