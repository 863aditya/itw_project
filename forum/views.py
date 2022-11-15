from django.shortcuts import render
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
from forum.models import fmsg
from univworks.models import students
# Create your views here.
LIMIT=5
def pg(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            a1=request.user.username
            a2=request.POST.get('description')
            a2=fmsg(posted_by=a1,content=a2)
            a2.save()
        q1=fmsg.objects.all()
        d1=dict()
        for x in range(len(q1)):
                d1[x+1]={'posted': q1[x].posted_by,'content':q1[x].content}

        a1=students.objects.filter(username=str(request.user.username))
        if len(a1)==0:
            return render(request,'forum.html',{'d1':d1})
        else:
            return render(request,'student_forum.html',{'d1':d1})
    return redirect('/p/')