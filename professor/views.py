from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
from professor.models import make_announcement,assignments
from pathlib import Path
import uuid
from hashlib import sha256

BASE_DIR = Path(__file__).resolve().parent.parent
# Create your views here.
# admin and admin

def handle_uploaded_file(f,z):  
    q=str(f.name)
    q=q.split('.')
    with open(str(BASE_DIR) +'/static/upload/'+z+ '.'+q[1], 'wb+') as destination:  
        for chunk in f.chunks():  
            destination.write(chunk)  



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
        title=request.POST.get('title')
        description=request.POST.get('description')
        file_assignment=request.FILES['file']
        dt=request.POST.get('deadline')
        print(file_assignment)
        a1=assignments(title_assignment=title,file_assignment=file_assignment,deadline_assignment=dt,message_assignment=description)
        # print(request.POST.file)
        print(request.FILES)
        handle_uploaded_file(request.FILES['file'],sha256(str(request.FILES['file']).encode('utf-8')).hexdigest())
        a1.save()
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
        d2["link"]=f"/static/upload/{sha256(str(request.FILES['file']).encode('utf-8')).hexdigest()}.{y[1]}"
        d1[x+1]=d2
    return render(request,'prof_assignments.html',{'d1':d1})


def ann(request):
    print(request.user.is_authenticated)
    if request.user.is_authenticated:
        # return render(request,'ann.html')
        if request.method=='POST':
            z=request.POST.get('title')
            y=request.POST.get('description')
            ay=make_announcement(title= z,content= y)
            ay.save()
        a1=make_announcement.objects.all()
        d1=dict()
        for x in range(len(a1)):
            d1[x+1]=[a1[x].title,a1[x].content,a1[x].date_posted]
        return render(request,'prof_announcement.html',{'d1':d1})

    else:
        return redirect('/p/')