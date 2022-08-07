from .models import CustomUser
from django.forms import ModelForm, TextInput, EmailInput, PasswordInput, CharField, EmailField, ImageField, ClearableFileInput
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm

class CustomUserCreationFrom(UserCreationForm):
    username = CharField(label = 'Никнейм', widget = TextInput(attrs={'class':'pas1'}))
    email = EmailField(label = 'Почта', widget = EmailInput(attrs={'class':'pas1'}))
    password1 = CharField(label = 'Пароль', widget = PasswordInput(attrs={'class':'pas1'}))
    password2 = CharField(label = 'Повторите пароль', widget = PasswordInput(attrs={'class':'pas2'}))
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2')

# class UserAuthenticationForm(AuthenticationForm):
#     username = CharField(label = 'Никнейм', widget = TextInput(attrs={'class':'pas1'}))
#     password = CharField(label = 'Пароль', widget = PasswordInput(attrs={'class':'pas1'}))

class CustomUserChangeFrom(UserChangeForm):
    username = CharField(label = 'Никнейм', widget = TextInput(attrs={'class':'pas1', 'value':'username'}))
    email = EmailField(label = 'Почта', widget = EmailInput(attrs={'class':'pas1'}))
    # image = ImageField(label = 'Изображение', widget = ClearableFileInput(attrs={'class':'pas1'}))
    # password = CharField(label = 'Пароль', widget = PasswordInput(attrs={'class':'pas1'}))
    class Meta:
        model = CustomUser
        fields = ['username', 'email']