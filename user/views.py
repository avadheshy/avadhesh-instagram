
from re import U
from traceback import print_tb
from django import urls
from django.shortcuts import redirect, render
from user.models import User
from core.models import Follow, Post, Comment, Like
from django.contrib.auth import logout

# Create your views here.


def logout(request):
    logout(request)
    return redirect('/')


def login(request):
    top5person = Post.objects.all().order_by('-created_on')

    personExceptMe = Follow.objects.filter(
        user__id=request.user.id).values('followed')
    non_followers_user_ids = []
    followe_id = []
    for user in personExceptMe:
        followe_id.append(user['followed'])
        non_followers_user_ids.append(user['followed'])
    non_followers_user_ids.append(request.user.id)
    non_followers = User.objects.exclude(
        id__in=non_followers_user_ids).values()
    personFollow = User.objects.filter(id__in=followe_id).values()
    follower_post = Post.objects.filter(user_id__in=followe_id)
    context = {
        'personFollow': personFollow,
        'user': request.user,
        'non_followers': non_followers,
        'follower_post': follower_post
    }

    return render(request, 'user/person.html', context)


def profile(request):
    user_post = Post.objects.filter(user=request.user).order_by('-created_on')
    post_count = Post.objects.filter(user=request.user).count()
    following_count = Follow.objects.filter(user=request.user).count()
    followers_count = Follow.objects.filter(followed=request.user).count()
    context = {
        'user_post': user_post,
        'post_count': post_count,
        'following_count': following_count,
        'followers_count': followers_count
    }
    return render(request, 'user/profile.html', context)


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
        like_count = Like.objects.filter(post=post_obj).count()
        user_comments = Comment.objects.filter(
            post=post_obj).order_by('commented_on')
        context = {
            'post_obj': post_obj,
            'like_count': like_count,
            'comments': user_comments,
        }
        return render(request, 'user/likes_comments.html', context)
    else:
        return redirect('login')


def likes(request, like_id):
    post_obj = Post.objects.get(id=like_id)
    user_obj = User.objects.get(username=request.user.username)
    new_like = Like(user=user_obj, post=post_obj)
    new_like.save()
    like_count = Like.objects.filter(post=post_obj).count()
    user_comments = Comment.objects.filter(
        post=post_obj).order_by('commented_on')
    context = {
        'post_obj': post_obj,
        'like_count': like_count,
        'comments': user_comments,
    }
    return render(request, 'user/likes_comments.html', context)


def follow(request, post_user_id):
    if request.method == 'POST':
        post_user_obj = User.objects.get(id=post_user_id)
        user_obj = User.objects.get(username=request.user.username)
        new_follow = Follow(user=user_obj, followed=post_user_obj)
        new_follow.save()
        return redirect('login')


def otherProfile(request, otherProfile_id):
    if request.method == 'POST':
        otherUser = User.objects.get(id=otherProfile_id)
        allPosts = Post.objects.filter(user=otherUser)
        following_count = Follow.objects.filter(user=otherUser).count()
        followers_count = Follow.objects.filter(followed=otherUser).count()
        postCount = len(allPosts)
        context = {
            'allPost': allPosts,
            'follow_count': following_count,
            'followers_count': followers_count,
            'otherProfile_id': otherProfile_id,
            'otherUser': otherUser,
            'postCount': postCount

        }
        return render(request, 'user/userProfile.html', context)


def unfollow(request, unfollow_id):
    if request.method == 'POST':
        followedUser = User.objects.filter(id=unfollow_id)
        print('hello')
        del_follower = Follow.objects.filter(
            user_id=request.user.id).filter(followed_id=unfollow_id)

        del_follower.delete()
        return redirect('login')


def followers(request):
    if request.method == 'POST':
        people = Follow.objects.filter(followed=request.user).values('user_id')
        following_id = []
        for person in people:
            following_id.append(person['user_id'])
        following = User.objects.filter(id__in=following_id)
        yourFollowers = []
        for people in following:
            yourFollowers.append(people)
        return render(request, 'user/followers.html', {'yourFollowers': yourFollowers})


def following(request):
    if request.method == 'POST':
        people = Follow.objects.filter(user=request.user).values('followed_id')
        people_id = []
        for per in people:
            people_id.append(per['followed_id'])
        ans = User.objects.filter(id__in=people_id)
        people_follow = []
        for abc in ans:
            people_follow.append(abc.username)
        return render(request, 'user/following.html', {'people_follow': people_follow})
