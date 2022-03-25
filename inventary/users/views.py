from django.shortcuts import render

from django.shortcuts import render
from django.http import HttpResponse
from .models import User

def index(request):
    user_list= User.objects.all()
    return render(request,"users/index.html",{
        "user_list":user_list
    })

def user(request, user_id):
    return HttpResponse(f"estas viedo el did del usuario {user_id}")

def information(request, user_id):
    return HttpResponse(f"Mas information del usuario {user_id}")

def createIdentificationNumber(request, identification_id):
    return HttpResponse(f"vas a crear un tipo de identificacion{identification_id}")

