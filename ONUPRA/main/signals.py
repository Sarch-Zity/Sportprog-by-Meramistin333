from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Competition
from django.utils.timezone import now, timedelta
from celery import Celery
from .tasks import checker

app = Celery('ONUPRA')

@receiver(post_save, sender=Competition)
def NewCompetition(**kwargs):
    eta_time = kwargs.get("instance").start_time + timedelta(minutes=kwargs.get("instance").duration)
    if kwargs.get("instance").actual:
        checker.apply_async(args=[kwargs.get("instance").id], eta=eta_time)