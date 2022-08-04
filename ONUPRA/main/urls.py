from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='home'),
    path('you/', views.account, name='account'),
    path('signup/', views.reg_page, name='signup'),
    # path('login/', views.login, name='login'),
    path('login/', auth_views.LoginView.as_view(template_name = 'main/login_form2.html'), name='login'),
]
