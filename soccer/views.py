from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# add function to test response.
def soccer(request):
    return HttpResponse("This is a test!")
