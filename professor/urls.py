from django.contrib import admin
from django.urls import path,include
from professor import views
urlpatterns = [
    path('',views.signin),
    path('home',views.home),
    path('ann',views.ann),
    path('prof_assignment',views.prof_assignment),
]