from django.contrib import admin
from django.urls import path,include
from students import views
urlpatterns = [
    path('home/',views.home),
    path('login/',views.login),
]