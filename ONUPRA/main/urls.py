from django.urls import path, register_converter
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # path('test/', views.testfunc, name='test'),
    path('', views.Index, name='home'),
    path('you/', views.Account_REDIR, name='you'),
    path('signup/', views.Registration, name='signup'),
    path('login/', views.Authentication, name='login'),
    path('logout/', views.Logout, name='logout'),
    path('settings/', views.Settings, name='edit'),
    path('top/', views.Top, name='top'),
    path('competition/', views.Competitions, name='competitions'),
    path('competition/<int:id>/', views.Сurrent_competition, name='сompetition'),
    path('competition/<int:id>/<int:taskid>/', views.Competition_now, name='competition_task'),
    path('party/<int:id>/', views.PartyRequest, name='party'),
    path('user/<str:username>/', views.Profile, name='account'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
