from .models import CustomUser
from django.forms import ModelForm, TextInput, EmailInput, PasswordInput, CharField, EmailField, ImageField, ClearableFileInput
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