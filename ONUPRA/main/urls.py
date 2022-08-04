from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('you/', views.account, name='account'),
    path('registration/', views.reg_page, name='reg_page'),
    path('login/', views.login, name='login'),
]
