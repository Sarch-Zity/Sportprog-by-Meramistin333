from django.contrib import admin
from .models import users, CustomUser

admin.site.register(users)
admin.site.register(CustomUser)
