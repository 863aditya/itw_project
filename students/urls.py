from django.contrib import admin
from django.urls import path,include
from students import views
urlpatterns = [
    path('home/',views.home),
    path('login/',views.login_x),
    path('',views.login_x),
    path('assignments/',views.vassignment),
    path('submit/<int:pk>',views.submit,name="submission"),
    path('ann',views.ann),
]