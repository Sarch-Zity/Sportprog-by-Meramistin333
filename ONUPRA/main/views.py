from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import users, CustomUser
from .forms import users_form, CustomUserCreationFrom

def index (request):
    return render(request, 'main/home.html')

def account (request):
    return render(request, 'main/user_page.html')

def reg_page (request):
    error = ''
    if request.method == 'POST':
        form = CustomUserCreationFrom(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            error = 'Error'

    form = CustomUserCreationFrom()
    content = {
        'form': form,
        'error': error
    }
    return render(request, 'main/registration_form.html', content)

def login (request):
    return render(request, 'main/login_form.html')