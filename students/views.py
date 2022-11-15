from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
from professor.models import make_announcement,assignments,exams
from pathlib import Path
import uuid
from hashlib import sha256
import datetime,time
# Create your views here.
from students.models import students_assignment
from univworks.models import students

BASE_DIR = Path(__file__).resolve().parent.parent

def handle_uploaded_file(f,z):  
    q=str(f.name)
    q=q.split('.')
    with open(str(BASE_DIR) +'/static/upload/'+z+ '.'+q[1], 'wb+') as destination:  
        for chunk in f.chunks():  
            destination.write(chunk)  



def home(request):
    if request.user.is_authenticated:
        return render(request,'student_base.html',{'name':request.user.username})
    return redirect('/s/login')

def login_x(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        print(user)
        if user is not None:
            login(request,user)
            return redirect('/s/home/')
        else:
            return redirect('/s/login/')
    return render(request,'student_sign.html')

def vassignment(request):
    a1=assignments.objects.all()
    d1=dict()
    roll_x=students.objects.filter(username=request.user.username)[0].roll

    for x in range(len(a1)):
        d2=dict()
        ax=students_assignment.objects.filter(assignments_id=a1[x].id,roll_number=roll_x)
        if len(ax)==0:
            ay=students_assignment(assignments_id=a1[x].id,roll_number=roll_x)
            ay.save()
        ax=students_assignment.objects.filter(assignments_id=a1[x].id,roll_number=roll_x)
        d2["title_assignment"]=a1[x].title_assignment
        d2["file_assignment"]=a1[x].file_assignment
        d2["deadline_assignment"]=a1[x].deadline_assignment
        d2["message_assignment"]=a1[x].message_assignment
        y=a1[x].file_assignment
        y=y.split('.')
        qw=a1[x].posted_on
        d2["link"]=f"/static/upload/{sha256(str(qw).encode('utf-8')).hexdigest()}.{y[1]}"
        d2["submit"]='/s/submit/'+str(a1[x].id)
        d2["check"]=ax[0].marks_reci=="no corrected"
        print(ax[0].marks_reci)
        d1[x+1]=d2
    return render(request,'student_assignment.html',{'d1':d1,'title_x':'Assignments'})
    pass

def submit(request,**kwargs):
    print(kwargs.get('pk'))
    assignment_id=kwargs.get('pk')
    roll_x=students.objects.filter(username=request.user.username)[0].roll
    obj=assignments.objects.filter(id=assignment_id)[0]
    d2=dict()
    d2["title_assignment"]=obj.title_assignment
    d2["file_assignment"]=obj.file_assignment
    d2["deadline_assignment"]=obj.deadline_assignment
    d2["message_assignment"]=obj.message_assignment
    d2["submit"]=str(obj.id)
    y=obj.file_assignment
    y=y.split('.')
    qw=obj.posted_on
    d2["link"]=f"/static/upload/{sha256(str(qw).encode('utf-8')).hexdigest()}.{y[1]}"
    d1={1:d2}
    if request.method=='POST':
        ax=students_assignment.objects.filter(assignments_id=assignment_id,roll_number=roll_x)
        ay=ax[0]
        file_taken=request.FILES['file']
        ay.marks_reci="no corrected"
        ay.submitted_on=datetime.datetime.now()
        ay.file_submitted=file_taken
        df=str(roll_x)+str(assignment_id)
        ay.file_name=sha256(str(df).encode('utf-8')).hexdigest()
        ay.save()
        handle_uploaded_file(file_taken,ay.file_name)
        return redirect('/s/assignments/')
    
    return render(request,'student_submit.html',{'d1':d1,'id':str(obj.id)})
    
    # pass