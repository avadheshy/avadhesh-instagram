import imp
from django import urls
from django.shortcuts import render
from user.models import User
from core.models import Post

# Create your views here.
def abc(request):
    obj=User.objects.all()
    top5person = Post.objects.all()[:5]
    # context={
    #     'person':obj,
    #     'fivePerson':top5person,

    # }
    
    return render(request,'user/person.html',{'top5person':top5person})
def posts(request):
    obj=Post.objects.all()
    context={
        'person':obj,
    }
    return render(request,'user/posts.html',context)