import imp
from django import urls
from django.shortcuts import render
from user.models import User
from core.models import Post

# Create your views here.
def abc(request):
    obj=User.objects.all()
    return render(request,'user/person.html',{'person':obj})
def posts(request):
    obj=Post.objects.all()
    context={
        'person':obj,
    }
    return render(request,'user/posts.html',context)