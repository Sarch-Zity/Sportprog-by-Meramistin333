from django.contrib import admin
from .models import CustomUser, Task, Competition, Attempt, Article, File

admin.site.register(CustomUser)
admin.site.register(Task)
admin.site.register(Competition)
admin.site.register(Attempt)
admin.site.register(Article)
admin.site.register(File)