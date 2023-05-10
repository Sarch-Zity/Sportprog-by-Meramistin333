from .models import CustomUser, Competition, Task, Article, File
from django.forms import ModelForm, TextInput, Textarea, EmailInput, PasswordInput, CharField, EmailField, ImageField, ClearableFileInput, NumberInput, FileInput, FileField, BooleanField, CheckboxInput
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm

class CustomUserCreationFrom(UserCreationForm):
    username = CharField(label = 'Никнейм', widget = TextInput())
    email = EmailField(label = 'Почта', widget = EmailInput())
    password1 = CharField(label = 'Пароль', widget = PasswordInput())
    password2 = CharField(label = 'Повторите пароль', widget = PasswordInput())
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2')

class CustomAuthenticationForm(AuthenticationForm):
    username = CharField(label = 'Никнейм', widget = TextInput())
    password = CharField(label = 'Пароль', widget = PasswordInput())
    remember_me = BooleanField(label = 'Запомнить меня', required=False, widget = CheckboxInput())
    class Meta:
        model = CustomUser
        fields = ('username', 'password', 'remember_me')

class CustomUserImageChangeFrom(UserChangeForm):
    image = ImageField(label = 'Изображение', widget = ClearableFileInput())
    class Meta:
        model = CustomUser
        fields = ['image']

class CustomUserUsernameChangeFrom(UserChangeForm):
    username = CharField(label = 'Никнейм', widget = TextInput())
    class Meta:
        model = CustomUser
        fields = ['username']

class PasswordChangeForm(ModelForm):
    old_password = CharField(label = 'Старый пароль', widget = PasswordInput())
    new_password = CharField(label = 'Новый пароль', widget = PasswordInput())
    new_password_repeat = CharField(label = 'Повторите новый пароль', widget = PasswordInput())
    class Meta:
        model = CustomUser
        fields = ['old_password', 'new_password', 'new_password_repeat']

class ArticleForm(ModelForm):
    text = CharField(label = 'Текст статьи', widget = Textarea())
    class Meta:
        model = Article
        fields = ['text']

class FileForm(ModelForm):
    files = FileField(label = 'Изображение', widget = FileInput(attrs = {'multiple': 'multiple'}))
    class Meta:
        model = File
        fields = ['files']
