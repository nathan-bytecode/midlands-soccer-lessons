from django.shortcuts import render
from django.views import generic
from .models import Account

# Create your views here.

def index(request):
    return render(request, 'soccer/index.html')

def account(request):
    return render(request, 'soccer/templates/account/signup.html')
