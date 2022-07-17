from email import message
from django.shortcuts import redirect, render
from user.models import User
from django.contrib import messages


# Create your views here.
def index(request):
    return render(request, 'authentication/index.html')
def register(request):
    return render(request,'authentication/register.html')


