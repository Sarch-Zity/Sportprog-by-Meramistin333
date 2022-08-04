from django.db import models
from django.contrib.auth.models import AbstractUser
import django

class CustomUser(AbstractUser):
    image = models.ImageField('Изображение', blank=True, null=True, upload_to='')
    rating = models.IntegerField('рейтинг', blank=True, default=0)
    email = models.EmailField('email address', max_length=254, unique=True, blank=False)
    username = models.CharField(help_text = '', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')
    