from email import message
from re import T
from django.shortcuts import redirect, render
from user.models import User
from django.contrib import messages
from core.models import Post


# Create your views here.
def person(request):
    return render(request,'authentication/person.html')
def index(request):
    print(request.method)
    if request.method=='POST':
        
        username=request.POST['username']
        password=request.POST['password']
        if User.objects.filter(username=username).exists():
            return redirect('login')
        else:
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

def posts(request):
    if request.method=='POST':
        text=request.POST['text']
        image=request.POST['image']
        print(text)
        post_obj=Post(text=text,image=image,user=request.user)
        post_obj.save()
        all_post=Post.objects.filter(user=request.user)
        return redirect('profile')

    else:
        return render(request,'user/posts.html')
