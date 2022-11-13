from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
from professor.models import make_announcement,assignments
 
# Create your views here.
# Create your views here.
def signin(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/p/home')
        else:
            return redirect('/p/')


    return render(request,'signin.html')

def home(request):
    return render(request,'prof_home.html')

def prof_assignment(request):
    pass
    a1=assignments.objects.all()
    d1=dict()
    for x in range(len(a1)):
        d1[x]=a1[x].title_assignment

    