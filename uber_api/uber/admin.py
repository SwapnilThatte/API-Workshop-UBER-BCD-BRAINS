from django.contrib import admin
from .models import User, Driver, Ride, UsrHistory
# Register your models here.
admin.site.register(User)
admin.site.register(Driver)
admin.site.register(Ride)
admin.site.register(UsrHistory)

