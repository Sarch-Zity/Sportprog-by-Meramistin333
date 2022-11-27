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
                if comp[i].rating:
                    user_dict = {}
                    max_xp = 0
                    for j in comp[i].tasks.all():
                        max_xp += j.score
                    for j in comp[i].determined_users.all():
                        user_xp = 0
                        print(j.user.all()[0].username)
                        for k in j.task.all():
                            q = k.attempts.order_by('-points')
                            print(q[0].points)
                            user_xp += q[0].points
                            print(user_xp)
                        user_dict[j.user.all()[0].username] = user_xp
                    sorted_user_dict = sorted(user_dict.values())[::-1]
                    for j in comp[i].determined_users.all():
                        user = j.user.all()[0]
                        index_u = user_dict[user.username]
                        place = sorted_user_dict.index(index_u)
                        place_coeff = (len(comp[i].determined_users.all()) - place) / len(comp[i].determined_users.all())
                        rating_coeff = user.rating / 5000
                        print('now')
                        print(user.rating)
                        print((place_coeff - rating_coeff) * 5000 / 2 + user.rating)
                        user.rating = int((place_coeff - rating_coeff) * 5000 / 2 + user.rating)
                        print(user.rating)
                        user.save()
            else:
                print(f"All okay, nearest end of competetion in {comp.end_time} (UTC)")
                break
    else:
        print('the list is empty')