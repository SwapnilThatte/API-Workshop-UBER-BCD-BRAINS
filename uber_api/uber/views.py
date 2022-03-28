from django.http import JsonResponse
from urllib import response
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, HttpResponse

# Create your views here.
@csrf_exempt
def newuser(request):
    if request.method == 'POST' :
        name = request.POST[name]
        print(f'\nname\n')
        pass


    return JsonResponse({"name" : "hello world !"})
    
