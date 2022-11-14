from django.shortcuts import render,redirect

# Create your views here.
from univworks.models import students
from univworks.forms import UserForm
def dummy(f,x):
    return f.changed_data[x]
def signup(request):
    if request.method=='POST':
        f1=UserForm(request.POST)
        if f1.is_valid():
            f1.save()
            a1=students(roll=dummy(f1,'roll_number'),email=dummy(f1,'email'),first_name=dummy(f1,'first_name'),last_name=dummy(f1,'last_name'),password=dummy(f1,'password1'))
            a1.save()
            
            redirect('/p/')
    form=UserForm
    return render(request,'register.html',{'form':form})