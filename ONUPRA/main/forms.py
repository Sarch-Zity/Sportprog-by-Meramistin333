from .models import CustomUser, Competition, Task
from django.forms import ModelForm, TextInput, EmailInput, PasswordInput, CharField, EmailField, ImageField, ClearableFileInput, DateTimeField
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm

class CustomUserCreationFrom(UserCreationForm):
    username = CharField(label = 'Никнейм', widget = TextInput())
    email = EmailField(label = 'Почта', widget = EmailInput())
    password1 = CharField(label = 'Пароль', widget = PasswordInput())
    password2 = CharField(label = 'Повторите пароль', widget = PasswordInput())
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2')

class CustomUserChangeFrom(UserChangeForm):
    username = CharField(label = 'Никнейм', widget = TextInput())
    email = EmailField(label = 'Почта', widget = EmailInput())
    image = ImageField(label = 'Изображение', widget = ClearableFileInput())
    class Meta:
        model = CustomUser
        fields = ['username', 'email']

class PasswordChangeForm(ModelForm):
    old_password = CharField(label = 'Старый пароль', widget = PasswordInput())
    new_password = CharField(label = 'Новый пароль', widget = PasswordInput())
    new_password_repeat = CharField(label = 'Повторите новый пароль', widget = PasswordInput())
    class Meta:
        model = CustomUser
        fields = ['old_password', 'new_password', 'new_password_repeat']

class CreateCompetitionForm(ModelForm):
    start_time = DateTimeField(label = 'Время старта', widget = TextInput())
    title = CharField(label = 'Название соревнования', widget = TextInput())

    class Meta:
        model = Competition
        fields = ['start_time', 'title']