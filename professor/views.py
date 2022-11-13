from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
from professor.models import make_announcement,assignments
 
# Create your views here.
# admin and admin
def signin(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        print(user)
        if user is not None:
            login(request,user)
            return redirect('/p/home')
        else:
            return redirect('/p/')

    # return render(request,'')
    return render(request,'signin.html')

def home(request):
    # if request
    return render(request,'prof_home.html')

def prof_assignment(request):
    if request.method=='POST':
        pass
    a1=assignments.objects.all()
    d1=dict()
    for x in range(len(a1)):
        d1[x]=a1[x].title_assignment


def ann(request):
    print(request.user.is_authenticated)
    if request.user.is_authenticated:
        # return render(request,'ann.html')
        if request.method=='POST':
            z=request.POST.get('title')
            y=request.POST.get('content')
            ay=make_announcement(z,y)
            ay.save()
        a1=make_announcement.objects.all()
        d1=dict()
        for x in range(len(a1)):
            d1[x]=[a1[x].title,a1[x].content,a1[x].date_posted]
        return render(request,'prof_announcement.html',{'d1':d1})

    else:
        return redirect('/p/')