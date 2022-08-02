from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('you/', views.account),
    path('registration/', views.reg_page),
]
