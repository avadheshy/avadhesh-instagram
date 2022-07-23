from django.urls import path
from user import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.login, name='login'),
    path('posts', views.posts, name='posts'),
    path('profile', views.profile, name='profile'),
    path('logout', views.logout, name='logout'),
    path('comments/<int:post_id>', views.comments, name='comments'),
    path('likes/<int:like_id>', views.likes, name='likes'),
    path('follow/<int:post_user_id>', views.follow, name='follow'),
    path('otherProfile/<int:otherProfile_id>',
         views.otherProfile, name='otherProfile'),
    path('otherProfile/unfollow/<int:unfollow_id>',
         views.unfollow, name='unfollow'),
    path('followers', views.followers, name='followers'),
    path('following', views.following, name='following'),
]
#urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
