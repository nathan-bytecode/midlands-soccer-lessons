from django.shortcuts import render
from django.views import generic
from .models import Account

# Create your views here.
def create_account(request):
    return render(request, 'soccer/account.html')
