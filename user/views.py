import imp
from django import urls
from django.shortcuts import redirect, render
from user.models import User
from core.models import Post

# Create your views here.
def login(request):
    obj=User.objects.all()
    top5person = Post.objects.all()[:5]
    return render(request,'user/person.html',{'top5person':top5person})
def posts(request):
    obj=Post.objects.all()
    context={
        'person':obj,
    }
    return render(request,'user/posts.html')
def profile(request):
    return redirect(request,'user/profile.html')