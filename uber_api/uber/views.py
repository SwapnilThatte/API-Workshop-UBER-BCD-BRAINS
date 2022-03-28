from django.http import JsonResponse
from urllib import response
from django.shortcuts import render, HttpResponse

# Create your views here.

def newuser(request):
    if request.method == 'POST' :
        name = request.POST[name]
        print(f'\nname\n')
        pass


    return JsonResponse({"name" : "hello world !"})
    
