from django.contrib import admin
from .models import Role,IdentificationType,People,User,Client

class PeopleAdmin(admin.ModelAdmin):
    list_display = ("id","first_name","last_name","email","identification_type","identification_number")
    search_fields=["identification_number","email"]

class UserAdmin(admin.ModelAdmin):
    list_display = ("id","user_name","rol")
    search_fields=["user_name"]
    list_filter=["rol"]

class ClientAdmin(admin.ModelAdmin):
    list_display = ("id","people")
    search_fields=["people"]

admin.site.register(Role)
admin.site.register(IdentificationType)
admin.site.register(People)
admin.site.register(User,UserAdmin)
admin.site.register(Client,ClientAdmin)

