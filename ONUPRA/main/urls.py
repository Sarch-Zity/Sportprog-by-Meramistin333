from django.urls import path, register_converter
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.index, name='home'),
    path('you/', views.accountREDIR, name='accountREDIR'),
    path('signup/', views.reg_page, name='signup'),
    path('login/', LoginView.as_view(template_name='main/login_form.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('edit/', views.AccountUpdate, name='edit2'),
    path('<slug:slug>/', views.AccountDetailView.as_view(), name='account'),
    path('<slug:slug>/edit/', views.AccountUpdateView.as_view(), name='edit'),
]
