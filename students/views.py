from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
from professor.models import make_announcement,assignments,exams
from pathlib import Path
import uuid
from hashlib import sha256
import datetime,time
# Create your views here.

def home(request):
    if request.user.is_authenticated:
        return render(request,'student_base.html',{'name':request.user.username})
    return redirect('/s/login')

def login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        print(user)
        if user is not None:
            login(request,user)
            return redirect('/s/home')
        else:
            return redirect('/s/login')
    return render(request,'signin.html')

def vassignment(request):
    a1=assignments.objects.all()
    d1=dict()
    for x in range(len(a1)):
        d2=dict()
        d2["title_assignment"]=a1[x].title_assignment
        d2["file_assignment"]=a1[x].file_assignment
        d2["deadline_assignment"]=a1[x].deadline_assignment
        d2["message_assignment"]=a1[x].message_assignment
        y=a1[x].file_assignment
        y=y.split('.')
        qw=a1[x].posted_on
        d2["link"]=f"/static/upload/{sha256(str(qw).encode('utf-8')).hexdigest()}.{y[1]}"
        d2["submit"]='/s/submit/'+str(a1[x].id)
        d1[x+1]=d2
    return render(request,'student_assignment.html',{'d1':d1,'title_x':'Assignments'})
    pass

def submit(request,**kwargs):
    print(kwargs.get('pk'))
    # pass