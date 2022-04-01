from django.urls import path
from . import views

app_name="users"
urlpatterns = [
    path("",views.index, name="index"),
    path("people/<int:people_id>",views.people, name="people"),
    path("createpeople/",views.form, name="form"),
    path("peoplecreated/",views.peopleFormResult, name="peopleFormResult"),
]