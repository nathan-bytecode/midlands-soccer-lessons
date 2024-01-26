from django.shortcuts import render
from django.views import generic
from .models import Account, Booking
from soccer.forms import BookingForm

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

def bookings(request):
    context = {}
    form = BookingForm()
    context['form'] = form
    return render(request, 'soccer/bookings.html', context)

# def new_booking(request, slug):
  #  model = Booking
   # template_name = 'soccer/bookings.html'
    #fields = ['first_name', 'last_name']
 
    #booking_form = BookingForm()
