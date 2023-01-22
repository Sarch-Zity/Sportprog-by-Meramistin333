from celery import Celery
from .models import Competition
from django.utils.timezone import now

app = Celery('ONUPRA')

@app.task(name='foo')
def foo():
    print('Hello world!')

@app.task(name='checker')
def cheker():
    comp = Competition.objects.filter(actual = True).order_by('start_time')
    if len(comp) > 0:
        for i in range(len(comp)):
            timeLeft = comp[i].duration - int((now() - comp[i].start_time).total_seconds() // 60)
            if timeLeft <= 0:
                print(f"He is dead ({i})")
                comp[i].actual = False
                comp[i].save()
                if comp[i].rating:
                    user_dict = {}
                    max_score = 0
                    for j in comp[i].tasks.all():
                        max_score += j.score
                    for j in comp[i].determined_users.all():
                        user_score = 0
                        print(j.user.all()[0].username)
                        for k in j.task.all():
                            q = k.attempts.order_by('-points')
                            print(q[0].points)
                            user_score += q[0].points
                            print(user_score)
                        user_count = len(comp[i].determined_users.all())
                        average_score = max_score / user_count
                        user_dict[j.user.all()[0].username] = user_score
                    for j in comp[i].determined_users.all():
                        user = j.user.all()[0]
                        user_score = user_dict[user.username]
                        # place = sorted_user_dict.index(index_u)
                        # place_coeff = (len(comp[i].determined_users.all()) - place) / len(comp[i].determined_users.all())
                        # rating_coeff = user.rating / 5000
                        if user.rating == 0:
                            user.rating = 200 * ((user_score / average_score - 1) / 3 + 1)
                        else:
                            user.rating = user.rating * ((user_score / average_score - 1) / 3 + 1)
                        user.save()
            else:
                print(f"All okay, nearest end of competetion in {timeLeft} (UTC)")
                break
    else:
        print('the list is empty')