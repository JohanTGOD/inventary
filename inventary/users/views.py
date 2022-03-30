from django.shortcuts import render,get_object_or_404

from django.shortcuts import render
from django.http import HttpResponse
from .models import User,People,IdentificationType

def index(request):
    user_list= People.objects.all()
    return render(request,"users/index.html",{
        "user_list":user_list
    })

def people(request, people_id):
    current_people=get_object_or_404(People,pk = people_id)
    return render(request,"users/people.html",{
        "current_people":current_people
    })

def form(request):
    return render(request,"users/peopleform.html")

def peopleFormResult(request):
    try:
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        #age = request.POST["age"]
        email = request.POST["email"]
        address = request.POST["address"]
        cellphone = request.POST["cellphone"]
        identication_number = IdentificationType.objects.get(pk=int(request.POST["identication_number"]))
        #identication_type = request.POST["identication_type"]
    except:
        return HttpResponse(f"Complete la información del formulario por favor")
    else:
        new_people = People(first_name=first_name,
        last_name=last_name,email=email,address=address,cellphone=cellphone,identification_type=identication_number)
        new_people.save()    
        return render(request,"users/peoplecreate.html")

def createIdentificationNumber(request, identification_id):
    return HttpResponse(f"vas a crear un tipo de identific∫acion{identification_id}")

