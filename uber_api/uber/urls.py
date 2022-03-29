from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.newuser, name='newuser'),
    path('driver', views.newDriver, name='newDriver'),
    path('ride', views.newRide, name='newRide'),
    path('history', views.usrHistory, name='usrHistory'),
]
