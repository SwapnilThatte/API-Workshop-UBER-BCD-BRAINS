from django.http import JsonResponse
from urllib import response
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, HttpResponse
from uber.models import User
# Create your views here.
@csrf_exempt
def newuser(request):
    if request.method == 'POST' :
        name = request.POST.get('name')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        password = request.POST.get('password')
        user = User(name=name, email=email, number=mobile, password=password )
        user.save()
    
    return JsonResponse({
        "status" : "SUCCESS" 
    })

def driver(request):
    if request.method == 'POST':
        return JsonResponse()
