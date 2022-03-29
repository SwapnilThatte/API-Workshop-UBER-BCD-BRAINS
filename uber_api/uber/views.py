from django.http import JsonResponse
from urllib import response
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, HttpResponse
from uber.models import User1, Driver, Ride, UsrHistory
import json

# Create your views here.

@csrf_exempt
def newuser(request):
    json_data = json.loads(request.body)
    if request.method == 'POST' :
        
        print(type(json_data))
        name = json_data['name']
        email = json_data['email']
        mobile = json_data['mobile']
        password = json_data['password']
        user = User1(name=name, email=email, number=mobile, password=password)
        user.save()
    
    return JsonResponse({
        "status" : "User Created" 
    })

@csrf_exempt
def newDriver(request):
    json_data = json.loads(request.body)
    if request.method == 'POST' :

        name = json_data['name']
        email = json_data['email']
        mobile = json_data['mobile']
        car_no = json_data['car_no']
        rating = json_data['rating']
        newDriver = Driver(name=name, email=email, number=mobile, car_no=car_no, rating= rating)
        newDriver.save()
    
    return JsonResponse({
        "status" : "Driver created" 
    })

@csrf_exempt
def newRide(request):
    json_data = json.loads(request.body)
    if request.method == 'POST' :
        usr = json_data['usr']
        usrid = User1.objects.get(name=usr)
        price = json_data['price']
        currentloc = json_data['current_loc']
        destination = json_data['destination']
        pickup = json_data['pickup']
        ride = Ride(usr= usrid ,price=price,current_loc=currentloc,destination=destination,pickup=pickup)
        ride.save()
    
    return JsonResponse({
        "status" : "Ride Confirmed" 
    })

@csrf_exempt
def usrHistory(request):
    json_data = json.loads(request.body)
    if request.method == 'GET' :
        usr = json_data['usr']
        usrid = User1.objects.get(name=usr)
        user_history = usrid.ride_set.all()
        lis =[]
        for uh in user_history:
            d = {
                "price" : uh.price,
                "current_loc": uh.current_loc,
                "destination" : uh.destination,
                "pickup" : uh.pickup
            }
            lis.append(d)
        print(lis)
        return JsonResponse(lis, safe=False)



def driver(request):
    if request.method == 'POST':
        return JsonResponse()
