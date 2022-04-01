from django.urls import path
from . import views

app_name = "sells"
urlpatterns = [
    #path("",views.SellView.as_view(), name="index"),
    path("",views.index, name="index"),
    path("sellform/",views.sellForm, name="sellform")
]
