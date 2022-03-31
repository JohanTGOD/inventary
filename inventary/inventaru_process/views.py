from re import template
from django.shortcuts import render
from django.http import HttpResponse
from .models import Product,Category,Supplier,StateProduct
from django.views import generic


class IndexView(generic.ListView):
    template_name="inventaru_process/listproducts.html"
    context_object_name = "all_products"
    
    def get_queryset(self):
        return Product.objects.order_by("-name")


#def index(request):
#    products=Product.objects.all()
#    return render(request,"inventaru_process/listproducts.html",{
#        "all_products":products
#    })
