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
    bookings = Booking.objects.all()
    return render(request, "soccer/profile.html", {'bookings': bookings})

def courses(request):
    return render(request, 'soccer/courses.html')

def bookings(request):
    context = {}
    form = BookingForm()
    if request.method =='POST':
        if 'submit' in request.POST:
            form = BookingForm(request.POST)
            if form.is_valid():
                form.save()
        context['form'] = form
    return render(request, 'soccer/bookings.html', {'form': BookingForm})