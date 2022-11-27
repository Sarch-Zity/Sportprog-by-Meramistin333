from django.urls import path, register_converter
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.Index, name='home'),
    path('you/', views.Account_REDIR, name='accountREDIR'),
    path('signup/', views.Reg_page, name='signup'),
    path('login/', LoginView.as_view(template_name='main/login_form.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('edit/', views.Account_REDIR, name='edit'),
    path('top/', views.Rating, name='top'),
    path('competition/', views.Competition_view, name='сompetitions_view'),
    path('competition/<int:id>/', views.Competition_page, name='сompetition'),
    path('competition/<int:id>/<int:task>/', views.Task_page, name='task'),
    path('createcompetition/', views.CreateCompetition, name='ccc'),
    path('user/<slug:slug>/', views.AccountPage, name='account'),

]
