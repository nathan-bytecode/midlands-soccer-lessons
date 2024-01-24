from django.shortcuts import render
from django.views import generic
from .models import Account

# Create your views here.

def index(request):
    return render(request, 'soccer/index.html')

def account(request):
    return render(request, 'soccer/templates/account/signup.html')

def profile(request):
    """
    renders profile page
    """
    return render(request, "soccer/profile.html")

def courses(request):
    return render(request, 'soccer/courses.html')
 
