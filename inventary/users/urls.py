from django.urls import path
from . import views

urlpatterns = [
    path("",views.index, name="index"),
    path("<int:user_id>/",views.user, name="user"),
    path("<int:user_id>/information/",views.information, name="information"),
    path("<int:identification_id>/create/",views.createIdentificationNumber, name="create")
]