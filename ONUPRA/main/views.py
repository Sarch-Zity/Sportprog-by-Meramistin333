from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import users
from .forms import users_form

def index (request):
    return render(request, 'main/home.html')

def account (request):
    return render(request, 'main/user_page.html')

def reg_page (request):
    error = ''
    if request.method == 'POST':
        form = users_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Error'

    form = users_form()
    content = {
        'form': form,
        'error': error
    }
    return render(request, 'main/registration_form.html', content)