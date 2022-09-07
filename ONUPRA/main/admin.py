from django.contrib import admin
from .models import CustomUser, Task, Competition, Determined

admin.site.register(CustomUser)
admin.site.register(Task)
admin.site.register(Competition)
admin.site.register(Determined)
