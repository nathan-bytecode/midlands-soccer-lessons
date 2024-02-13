from django.shortcuts import render
from django.views import generic
from .models import Account, Booking
from soccer.forms import BookingForm
from django.contrib.auth.models import User


# Create your views here.

def index(request):
    return render(request, 'soccer/index.html')

def account(request):
    return render(request, 'soccer/templates/account/signup.html')

def profile(request):
    """
    renders profile page
    """
    context = {}
    form = BookingForm()
    bookings = Booking.objects.all()
    if 'save' in request.POST:
        form = BookingForm(request.POST)
    if form.is_valid():
        form.save()
    elif 'delete' in request.POST:
        pk = request.POST.get('delete')
        booking = Booking.objects.get(id=pk)
        booking.delete()
    elif 'edit' in request.POST:
        pk = request.POST.get('edit')
        booking = Booking.objects.get(id=pk)
        form = BookingForm(instance=booking) 
    context['form'] = form
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
                form.instance.user = (
                User.objects.get(username=request.user))
                form.save()
                print("form saved")
            elif 'delete' in request.POST:
                pk = request.POST.get('delete')
                print('other')
        else:
            print("form not saved or started", request.POST)
    
        context['form'] = form
    return render(request, 'soccer/bookings.html', {'form': BookingForm})