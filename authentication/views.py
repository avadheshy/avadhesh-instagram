from django.contrib.auth import authenticate
from django.shortcuts import redirect, render
from user.models import User
from django.contrib import messages
from core.models import Post
from django.contrib.auth import login


# Create your views here.
def person(request):
    return render(request,'authentication/person.html')
def index(request):
    if request.method=='POST':
        print('POst')
        username=request.POST['username']
        password=request.POST['password']
        print(username,password)
        user=User.objects.filter(username=username)
        
        if user is not None:
            login(request, user)
            print('hello')
            return redirect('login')
        else:
            print('hi')
            return redirect('/')
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


