import imp
from django import urls
from django.shortcuts import redirect, render
from user.models import User
from core.models import Post

# Create your views here.
def login(request):
    obj=User.objects.all()
    top5person = Post.objects.all()
    return render(request,'user/person.html',{'top5person':top5person})

def profile(request):
    return redirect(request,'user/profile.html')
def posts(request):
    if request.method=='POST':
        print('kajal')
        text=request.POST['text']
        image=request.POST['image']

        post_obj=Post(text=text,image=image,user=request.user)
        post_obj.save()
        
        return redirect('login')

    else:
        return render(request,'user/posts.html')