from django.shortcuts import render,redirect
from django.contrib.auth import logout, authenticate, login
# Create your views here.
from univworks.models import students
from univworks.forms import UserForm
def dummy(request,x):
    return request.POST.get(x)
def signup(request):
    if request.method=='POST':
        f1=UserForm(request.POST)
        if f1.is_valid():
            a1=request.POST.get('username')
            print(a1)
            a1=students(roll=dummy(request,'roll_number'),email=dummy(request,'email'),first_name=dummy(request,'first_name'),last_name=dummy(request,'last_name'),password=dummy(request,'password1'),username=dummy(request,'username'))
            a1.save()
            f1.save()

            return redirect('/s/home')
    form=UserForm
    return render(request,'register.html',{'form':form})

def signout(request):
    logout(request)
    return redirect('/')

def home(request):
    return render(request,'univ_home.html')