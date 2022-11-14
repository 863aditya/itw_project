from django.shortcuts import render,redirect

# Create your views here.

def home(request):
    if request.user.is_authenticated:
        return render(request,'student_home.html')
    return redirect('/s/login')

def login(request):
    return render(request,'signin.html')