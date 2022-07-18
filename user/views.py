import imp
from django import urls
from django.shortcuts import render
from user.models import User
from core.models import Post

# Create your views here.
def abc(request):
    obj=User.objects.all()
    context={
        'person':obj,
        'posts':Post.objects.all()
    }
    return render(request,'user/person.html',context)
def posts(request):
    obj=Post.objects.all()
    context={
        'person':obj,
    }
    return render(request,'user/posts.html',context)