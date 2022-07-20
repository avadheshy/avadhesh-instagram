import imp
from django import urls
from django.shortcuts import redirect, render
from user.models import User
from core.models import Post
from django.contrib.auth import logout

# Create your views here.


def logout(request):
    logout(request)
    return redirect('/')


def login(request):
    obj = User.objects.all()
    top5person = Post.objects.all().order_by('-created_on')
    return render(request, 'user/person.html', {'top5person': top5person})


def profile(request):
    return redirect(request, 'user/profile.html')


def posts(request):
    if request.method == 'POST':
        text = request.POST['text']
        image = request.FILES['img']

        post_obj = Post(text=text, img=image, user=request.user)
        post_obj.save()

        return redirect('login')

    else:
        return render(request, 'user/posts.html')
