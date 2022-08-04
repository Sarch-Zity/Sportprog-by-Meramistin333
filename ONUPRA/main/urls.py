from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('you/', views.account, name='account'),
    path('signup/', views.reg_page, name='signup'),
    path('login/', views.login, name='login'),
]
