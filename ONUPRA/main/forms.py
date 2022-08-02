from .models import users
from django.forms import ModelForm, TextInput, EmailInput, PasswordInput

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