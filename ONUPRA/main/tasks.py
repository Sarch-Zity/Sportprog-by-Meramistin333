from celery import Celery
from .models import Competition
from django.utils.timezone import now

app = Celery('ONUPRA')

@app.task(name='foo')
def foo():
    print('Hello world!')

@app.task(name='checker')
def cheker():
    comp = Competition.objects.filter(actual = True).order_by('end_time')
    if len(comp) > 0:
        for i in range(len(comp)):
            if comp[i].end_time <= now():
                print(f"He is dead ({i})")
                comp[i].actual = False
                comp[i].save()
            else:
                print(f"All okay, nearest end of competetion in {comp.end_time} (UTC)")
                break
    else:
        print('the list is empty')