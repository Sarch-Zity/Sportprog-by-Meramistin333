from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import CustomUser
from .forms import CustomUserCreationFrom
from django.contrib.auth import login, logout
from django.views.generic import DetailView

def index (request):
    return render(request, 'main/home.html')

class AccountDetailView(DetailView):
    print(CustomUser.username, "hi")
    model = CustomUser
    template_name = 'main/user_page.html'
    context_object_name = 'form'

def account (request):
    print(request.user.username)
    return render(request, 'main/user_page.html')

def reg_page (request):
    if request.user.is_authenticated:
        return redirect('account')
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
            return redirect('account')
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