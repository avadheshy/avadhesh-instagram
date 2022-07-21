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
    user_post=Post.objects.filter(user=request.user).order_by('created_on')
    post_count=Post.objects.filter(user=request.user).count()
    context={
        'user_post':user_post,
        'post_count':post_count,
    }
    return render(request, 'user/profile.html',context)


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
        text = request.POST['text']
        post_obj = Post.objects.get(id=post_id)
        user_obj = User.objects.get(username=request.user.username)
        new_comment = Comment(text=text, user=user_obj, post=post_obj)
        new_comment.save()
        # print('new comment is saved in ')
        like_count=Like.objects.filter(post=post_obj).count()
        user_comments=Comment.objects.filter(post=post_obj).order_by('commented_on')
        context={
        'post_obj':post_obj,
        'like_count':like_count,
        'comments':user_comments,
         }
        return render(request,'user/likes_comments.html',context)
    else:
        return redirect('login')


def likes(request, like_id):
    post_obj = Post.objects.get(id=like_id)
    user_obj = User.objects.get(username=request.user.username)
    new_like = Like(user=user_obj, post=post_obj)
    new_like.save()
    like_count=Like.objects.filter(post=post_obj).count()
    user_comments=Comment.objects.filter(post=post_obj).order_by('commented_on')
    context={
        'post_obj':post_obj,
        'like_count':like_count,
        'comments':user_comments,
    }
    return render(request,'user/likes_comments.html',context)
