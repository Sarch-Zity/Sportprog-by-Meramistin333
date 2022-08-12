from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import CustomUser
from .forms import CustomUserCreationFrom, CustomUserChangeFrom
from django.contrib.auth import login, logout
from django.views.generic import DetailView, UpdateView 

def index (request):
    return render(request, 'main/home.html')

class AccountDetailView(DetailView):
    model = CustomUser
    template_name = 'main/user_page.html'
    context_object_name = 'form'

def AccountUpdate (request):
    error = ''
    if request.method == "POST":
        form = CustomUserChangeFrom(request.POST)
        if form.is_valid():
            request.user.slug = request.user.username
            request.user.save()
            print(request.user.slug)
            return redirect('account', request.user.slug)
        else:
            error = "Неизвестная нам ошибка"

    form = CustomUserChangeFrom()
    content = {
        'form': form,
        'error': error
    }
    return render(request, 'main/custom_profile_form.html', content)

def accountREDIR (request):
    return redirect('account', request.user.slug)

def reg_page (request):
    if request.user.is_authenticated:
        return redirect('account', request.user.slug)
    error = ""
    error_username = ""
    error_email = ""
    if request.method == 'POST':
        form = CustomUserCreationFrom(request.POST)
        email = request.POST.get('email')
        nickname = request.POST.get('username')
        if CustomUser.objects.filter(username=nickname).exists():
            error_username = "Данное имя уже занято"
        if CustomUser.objects.filter(email=email).exists():
            error_email = "Данный адрес электронной почты уже занято"
        if CustomUser.objects.filter(email=email).exists():
            error_email = "Данный адрес электронной почты уже занято"
        if form.is_valid():
            formsv = form.save()
            login(request, formsv)
            request.user.slug = request.user.username
            request.user.save()
            return redirect('accountREDIR')
        elif error_email == "" and error_username == "":
            error = "Неизвестная нам ошибка"

    form = CustomUserCreationFrom()
    content = {
        'form': form,
        'error': error,
        'error_username': error_username,
        'error_email': error_email
    }
    return render(request, 'main/registration_form.html', content)