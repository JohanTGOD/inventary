from django.shortcuts import render
from django.http import HttpResponse
from .models import Product,Category,Supplier,StateProduct

def index(request):
    products=Product.objects.all()
    return render(request,"inventaru_process/index.html",{
        "all_products":products
    })
