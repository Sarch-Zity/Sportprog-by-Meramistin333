from .models import users, CustomUser
from django.forms import ModelForm, TextInput, EmailInput, PasswordInput, CharField, EmailField
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class users_form(ModelForm):
    class Meta:
        model = users
        fields = ["nick", "email", "password"]
        widgets = {"nick":TextInput(attrs={

        }),
        "email":TextInput(attrs={

        }),
        "password":TextInput(attrs={

        }),}

class CustomUserCreationFrom(UserCreationForm):
    username = CharField(label = 'Никнейм', widget = TextInput(attrs={'class':'pas1'}))
    email = EmailField(label = 'Почта', widget = EmailInput(attrs={'class':'pas1'}))
    password1 = CharField(label = 'Пароль', widget = PasswordInput(attrs={'class':'pas1'}))
    password2 = CharField(label = 'Повторите пароль', widget = PasswordInput(attrs={'class':'pas2'}))
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2')
        widgets = {
        "username":TextInput(attrs={

        }),
        "email":TextInput(attrs={
            
        }),
        "password1":PasswordInput(attrs={
            'class': 'Kto'
        }),}

class CustomUserChangeFrom(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ["username", "email",]
        widgets = {
        "username":TextInput(attrs={
        }),
        "email":TextInput(attrs={
        }),}