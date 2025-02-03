from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.oneCity, name='main'),
    path('findcity/', views.oneCity, name='findcity'),
    path('ip/', views.get_client_ip, name='ip')
]
