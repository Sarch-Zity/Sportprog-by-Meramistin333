from django.db import models
from django.contrib.auth.models import AbstractUser
import django
from django.utils.timezone import timedelta
from autoslug import AutoSlugField
from PIL import Image

class CustomUser(AbstractUser):
    image = models.ImageField('Изображение', blank=True, null=True, default='default.png', upload_to='img/')
    rating = models.IntegerField('Рейтинг', blank=True, default=0)
    email = models.EmailField('Адрес электронной почты', max_length=254, unique=True, blank=False)
    username = models.CharField(help_text = '', max_length=32, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')
    slug = AutoSlugField(populate_from='username')
    
    def get_absolute_url(self):
        return redirect('accountRED')
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 250 or img.width > 250:
            output_size = (250, 250)
            img.thumbnail(output_size)
            img.save(self.image.path)

class Attempt(models.Model):
    time = models.DateTimeField('Время отправки')
    points = models.PositiveIntegerField('Количество полученых очков')
    successfully = models.BooleanField('Успешное решение', default=False)
    error = models.CharField('Ошибка', max_length=30) #1 - time error, 2 = returncode 0, 3 - incorrect answer (3-1)(1 - run number)

    def __str__(self):
        return str(self.points)

class Task(models.Model):
    title = models.CharField('Название задания', max_length=30)
    description = models.TextField('Описание задания')
    input_exmaple = models.TextField('Пример ввода кода')
    output_exmaple = models.TextField('Пример ввода кода')
    extra_text = models.TextField('Дополнительные пояснение, недочеты', blank=True)
    input_values = models.TextField('Вводимые значения')
    output_values = models.TextField('Получаемые значения')
    score = models.PositiveIntegerField('Количество очков за задание', help_text = 'Указывать половину от максимального числа')

    def __str__(self):
        return self.title

class AttemptTask(models.Model):
    task = models.ManyToManyField(Task)
    attempts = models.ManyToManyField(Attempt)

    def __str__(self):
        return str(self.task)

class Determined(models.Model):
    user = models.ManyToManyField(CustomUser)
    task = models.ManyToManyField(AttemptTask)

    def __str__(self):
        return str(self.user)

class Competition(models.Model):
    creation_date = models.DateTimeField('Дата создания', auto_now_add=True)
    start_time = models.DateTimeField('Дата старта')
    duration = models.PositiveIntegerField('Длительность соревнования') # минимум 30
    title = models.CharField('Название', unique=True, max_length=30)
    tasks = models.ManyToManyField(Task)
    actual = models.BooleanField('Не закончен', default=True)
    verified = models.BooleanField('Проверено администратором', default=False)
    rating = models.BooleanField('Рейтинговое ли соревнование', default=False)
    rating_points = models.PositiveIntegerField('Количество очков рейтнга', default=0)
    determined_users = models.ManyToManyField(Determined, blank=True)

    def __str__(self):
        return self.title

class Article(models.Model):
    text = models.CharField('О чем вы хотите рассказать?', max_length=500, blank=True, null=True)
    creation_date = models.DateTimeField('Дата создания', auto_now_add=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.user) + ' at ' + str(self.creation_date) + ' ' + str(self.text)[0:9]

class File(models.Model):
    creation_date = models.DateTimeField('Дата создания', auto_now_add=True)
    article = models.ForeignKey(Article, related_name='files', on_delete=models.CASCADE)
    files = models.FileField(upload_to='article_files/', null=True)
    
    def __str__(self):
        return str(self.creation_date) + ' and ' + str(self.article)

