from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import CustomUser
from .forms import CustomUserCreationFrom, CustomUserChangeFrom
from django.contrib.auth import login, logout
from django.views.generic import DetailView, UpdateView 

def index (request):
    print(request.user.username)
    return render(request, 'main/home.html')

def getname (request):
    return request.user.username

class AccountDetailView(DetailView):
    model = CustomUser
    template_name = 'main/user_page.html'
    context_object_name = 'form'

def AccountUpdate (request):
    print(request.user)
    print(request.user.username)
    error = ''
    if request.method == "POST":
        form = CustomUserChangeFrom(request.POST)
        if form.is_valid():
            request.user.username = request.POST.get('username')
            request.user.slug = request.user.username
            request.user.save()
            print(request.user.slug)
            return redirect('account', str(request.user))
        else:
            error = "Неизвестная нам ошибка"

    form = CustomUserChangeFrom()
    content = {
        'form': form,
        'error': error
    }
    return render(request, 'main/custom_profile_form.html', content)

class AccountUpdateView(UpdateView):
    model = CustomUser
    template_name = 'main/custom_profile_form.html'
    form_class = CustomUserCreationFrom

def accountREDIR (request):
    return redirect('account', str(request.user))

def reg_page (request):
    if request.user.is_authenticated:
        return redirect('account', str(request.user))
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
            CUser = CustomUser.objects.get(slug='')
            CUser.slug = str(CUser)
            CUser.save()
            print(CUser.slug)
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

def logout_user(request):
    logout(request)
    return redirect('home')

# def login (request):
#     error = ''
#     if request.method == 'POST':
#         form = UserAuthenticationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('login')
#         else:
#             error = 'Error'

#     form = UserAuthenticationForm()
#     content = {
#         'form': form,
#         'error': error
#     }
#     return render(request, 'main/login_form.html', content)