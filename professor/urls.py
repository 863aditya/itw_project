from django.contrib import admin
from django.urls import path,include
from professor import views
urlpatterns = [
    path('',views.signin),
    path('home',views.home),
    path('ann',views.ann),
    path('prof_assignment',views.prof_assignment),
    path('prof_exams',views.prof_exams),
    path('marking/<int:pk>/',views.marking),
    path('marking/<int:pk>/<str:roll>/',views.marking),
    path('main_marking/',views.main_marking),
]