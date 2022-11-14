from django.shortcuts import render
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
from forum.models import fmsg
 
# Create your views here.

def pg(request):
    if request.user.is_authenticated():
        if request.method=='POST':
            pass
        pass
    pass