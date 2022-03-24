from django.contrib import admin
from .models import Role,IdentificationType,People,User,Client

admin.site.register(Role)
admin.site.register(IdentificationType)
admin.site.register(People)
admin.site.register(User)
admin.site.register(Client)

