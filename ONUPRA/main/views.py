from django.shortcuts import render
from django.http import HttpResponse

def index (request):
    return render(request, 'main/index.html')

def account (request):
    return render(request, 'main/user_page.html')

def reg_page (request):
    return render(request, 'main/registration_form.html')