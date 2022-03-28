from django.http import JsonResponse
from urllib import response
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, HttpResponse
from uber.models import User1
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
        "status" : "SUCCESS" 
    })

def driver(request):
    if request.method == 'POST':
        return JsonResponse()
