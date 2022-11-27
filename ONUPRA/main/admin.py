from django.contrib import admin
from .models import CustomUser, Task, Competition, Attempt, AttemptTask, Determined, Article, File

admin.site.register(CustomUser)
admin.site.register(Task)
admin.site.register(Competition)
admin.site.register(Attempt)
admin.site.register(AttemptTask)
admin.site.register(Determined)
admin.site.register(Article)
admin.site.register(File)