from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic
from .models import Account, Booking
from soccer.forms import BookingForm
from django.contrib.auth.models import User
from django.contrib import messages


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
        booking = Booking.objects.get(id = pk)
        booking.delete()
    elif 'edit' in request.POST:
        pk = request.POST.get('edit')
        booking = Booking.objects.get(id = pk)
        form = BookingForm(instance = booking) 
    context['form'] = form
    return render(request, "soccer/profile.html", {'bookings': bookings})


def edit_booking(request, booking_id):
    booking = get_object_or_404(Booking, id = booking_id)
    form = BookingForm(instance = booking)
    if request.POST:
        form = BookingForm(request.POST, instance = booking)
        if form.is_valid():
            # save method called upon to update booking info #
            form.save()
            # upon update, message displays to nofify user #
            messages.success(request,
                'Your booking request has been updated.')
        return redirect('profile')
    booking = BookingForm(instance = booking)
    context = {
        'form': form }
    return render(request, 'soccer/edit_booking.html', context)


def delete_booking(request, booking_id):
    booking = get_object_or_404(Booking, id = booking_id)
    booking.delete() # delete method called upon to cancel user's booking #
    messages.warning(request,
        'Your booking has been cancelled.')
    return redirect('profile')


def courses(request):
    return render(request, 'soccer/courses.html')


def bookings(request):
    context = {}
    form = BookingForm()
    if request.method == 'POST':
        if 'submit' in request.POST:
            form = BookingForm(request.POST)
            if form.is_valid():
                form.instance.user = (
                User.objects.get(username = request.user))
                form.save()
                print("form saved")
            elif 'delete' in request.POST:
                pk = request.POST.get('delete')
                print('other')
        else:
            print("form not saved or started", request.POST)
            context['form'] = form
    return render(request, 'soccer/bookings.html', {'form': BookingForm})