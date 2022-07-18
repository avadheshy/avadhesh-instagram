from django.urls import path
from user import views

urlpatterns = [
    path('',views.abc, name='abc'),
    path('posts',views.posts,name='posts')

]