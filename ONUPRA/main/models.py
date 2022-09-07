from django.db import models
from django.contrib.auth.models import AbstractUser
import django
from django.utils.timezone import timedelta

class CustomUser(AbstractUser):
    image = models.ImageField('Изображение', blank=True, null=True, default='/main/media/default.png', upload_to='img/')
    rating = models.IntegerField('Рейтинг', blank=True, default=0)
    email = models.EmailField('Адрес электронной почты', max_length=100, unique=True, blank=False)
    username = models.CharField(help_text = '', max_length=25, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')
    slug = models.SlugField(unique = True, default = '')
    
    def get_absolute_url(self):
        return redirect('accountRED')

class Determined(models.Model):
    determined_users = models.ManyToManyField(CustomUser)
    time = models.DateTimeField('Время отправки')
    points = models.PositiveIntegerField('Количество полученых очков')
    successfully = models.BooleanField('Успешное решение', default=False)
    error = models.CharField('Ошибка', max_length=30) #1 - time error, 2 = returncode 0, 3 - incorrect answer (3-1)(1 - run number)

    def __str__(self):
        return str(self.successfully)

class Task(models.Model):
    title = models.CharField('Название задания', max_length=30)
    description = models.TextField('Описагие задания')
    input_exmaple = models.TextField('Пример ввода кода')
    output_exmaple = models.TextField('Пример ввода кода')
    extra_text = models.TextField('Дополнительные пояснение, недочеты', blank=True)
    input_values = models.TextField('Вводимые значения')
    output_values = models.TextField('Получаемые значения')
    soft = models.BooleanField('Чувтствительность к пробелам', default=False)
    determined_users = models.ManyToManyField(Determined, blank=True)
    score = models.PositiveIntegerField('Количество очков за задание', help_text = 'Указывать половину от максимального числа')

    def __str__(self):
        return self.title

class Competition(models.Model):
    creation_date = models.DateTimeField('Дата создания',auto_now_add=True)
    start_time = models.DateTimeField('Дата старта')
    duration = models.PositiveIntegerField('Длительность соревнования') # минимум 30
    end_time = models.DateTimeField('Дата окончания', blank=True)
    title = models.CharField('Название', unique=True, max_length=30)
    tasks = models.ManyToManyField(Task)
    actual = models.BooleanField('Не закончен', default=True)
    verified = models.BooleanField('Проверено администратором', default=False)
    rating = models.BooleanField('Рейтинговое ли соревнование', default=False)
    rating_points = models.PositiveIntegerField('Количество очков рейтнга', default=0)

    def __str__(self):
        return self.title