from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Sell,PaymentType
from django.views import generic
from users.models import User,Client
from inventaru_process.models import Product
from django.urls import reverse


#class SellView(generic.DetailView):
#    model = Sell
#    template_name = "sells/sellform.html"

def index(request):
    return render(request,"sells/sellform.html")    

def sellForm(request):
    try:
        print("Estoy por aca∫")
        client = Client.objects.get(pk=int(request.POST["client"]))
        product = Product.objects.get(pk=int(request.POST["product"]))
        payment_type = PaymentType.objects.get(pk=int(request.POST["payment_type"]))
        user = User.objects.get(pk=int(request.POST["user"]))
        quantity = request.POST["quantity"]
    except:
        return HttpResponse(f"Complete la información para realizar la venta")
    else:
        new_venta = Sell(client=client,product=product,payment_type=payment_type,user=user,quantity=quantity)    
        new_venta.save()
        print("Exitoso hasta acá")
        print((int(product.cuanity)-int(quantity)))
        product.cuanity=(int(product.cuanity)-int(quantity))
        product.save(update_fields=["cuanity"])    
        return HttpResponseRedirect(reverse("inventaryUrl:index"))
