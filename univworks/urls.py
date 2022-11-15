from django.contrib import admin
from django.urls import path,include
from univworks import views
urlpatterns = [
    path('s/signup', views.signup),
    path('s/signout/', views.signout),
    path('',views.home),
]
