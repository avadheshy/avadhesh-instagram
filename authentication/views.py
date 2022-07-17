from email import message
from django.shortcuts import redirect, render
from user.models import User
from django.contrib import messages


# Create your views here.
def person(request):
    return render(request,'authentication/person.html')
def index(request):
    if request.method=='POST':
        print("hai")
        username=request.POST['username']
        password=request.POST['password']
        if User.objects.filter(username=username).exists():
            print("hello")
            return redirect('person')
        else:
            return redirect('register')
    else:

        return render(request,'authentication/index.html')
def register(request):
    if request.method=='POST':
        full_name=request.POST['full_name']
        username=request.POST['username']
        password=request.POST['password']
        email=request.POST['email']
        new_user=User(email=email,full_name=full_name,
        username=username, password=password)
        new_user.save()
        return redirect('/')
        
    return render(request,'authentication/register.html')


