from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.mainPage, name='main'),
    path('findcity/', views.oneCity, name='findcity')
]
