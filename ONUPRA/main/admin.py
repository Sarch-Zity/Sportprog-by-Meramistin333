from django.contrib import admin
from .models import CustomUser, Task, Competition, Attempt, ScorePoint, Party

admin.site.register(CustomUser)
admin.site.register(Task)
admin.site.register(Competition)
admin.site.register(Attempt)
admin.site.register(ScorePoint)
admin.site.register(Party)