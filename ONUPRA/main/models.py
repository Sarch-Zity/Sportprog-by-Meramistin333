from django.db import models

class users(models.Model):
    nick = models.CharField('Имя', max_length=16)
    email = models.EmailField('Почта')
    password = models.CharField('Пароль', max_length=24)
    image = models.ImageField('Изображение', blank=True, null=True, upload_to='')
    rating = models.IntegerField('рейтинг', blank=True, default=0)

    def __str__(self):
        return self.nick