from django.urls import path
from authentication import views

urlpatterns = [
    path('',views.index, name='index'),
    path('register',views.register,name='register'),
    path('person',views.person,name='person'),
]