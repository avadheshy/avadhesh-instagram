import imp
from django import urls
from django.shortcuts import redirect, render
from user.models import User
from core.models import Post, Comment, Like
from django.contrib.auth import logout

# Create your views here.


def logout(request):
    logout(request)
    return redirect('/')


def login(request):
    top5person = Post.objects.all().order_by('-created_on')
    return render(request, 'user/person.html', {'top5person': top5person})


def profile(request):
    return render(request, 'user/profile.html')


def posts(request):
    if request.method == 'POST':
        text = request.POST['text']
        image = request.FILES['img']

        post_obj = Post(text=text, img=image, user=request.user)
        post_obj.save()

        return redirect('login')

    else:
        return render(request, 'user/posts.html')


def comments(request, post_id):

    if request.method == 'POST':
        post_obj = Post.objects.get(id=post_id)
        user_obj = User.objects.get(username=request.user.username)
        print(user_obj)
        new_like = Like(user=user_obj, post=post_obj)
        new_like.save()
        print('new liked is saved')
        redirect('/')
    else:
        print('else')
        redirect('/')


def likes(request, like_id):
    post_obj = Post.objects.get(id=like_id)
    user_obj = User.objects.get(username=request.user.username)
    new_like = Like(user=user_obj, post=post_obj)
    new_like.save()
    print('new like is saved')
    redirect('')

