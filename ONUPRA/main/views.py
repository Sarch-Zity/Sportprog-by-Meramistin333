from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import users, CustomUser
from .forms import users_form, CustomUserCreationFrom

def index (request):
    return render(request, 'main/home.html')

def account (request):
    return render(request, 'main/user_page.html')

def reg_page (request):
    error = [""]
    if request.method == 'POST':
        form = CustomUserCreationFrom(request.POST)
        email = request.POST.get('email')
        nickname = request.POST.get('username')
        if CustomUser.objects.filter(username=nickname).exists():
            error.append("Ник error")
        if CustomUser.objects.filter(email=email).exists():
            error.append("Почта error")
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            error.append("error")

    form = CustomUserCreationFrom()
    content = {
        'form': form,
        'error': error
    }
    print(error)
    return render(request, 'main/registration_form.html', content)

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