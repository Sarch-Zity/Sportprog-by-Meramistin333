from django.urls import path, register_converter
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('', views.index, name='home'),
    path('you/', views.account, name='account'),
    path('signup/', views.reg_page, name='signup'),
    path('login/', LoginView.as_view(template_name='main/login_form.html'), name='login'),
    path('logout/', views.logout, name='logout'),
    path('<str:pk>/', views.AccountDetailView.as_view(), name='account'),
]
