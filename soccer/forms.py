from django import forms
from datetime import datetime
from django.urls import reverse_lazy
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from soccer.models import Booking, Account, User
from django.forms import ModelForm



class BookingForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.add_input(Submit('submit', 'Submit'))

    class Meta:
        model = Booking
        fields = ['first_name', 'last_name', 'course_selection', 'venue_selection', 'email', 'contact_phone',
                  'booking_date', 'booking_time', 'number_of_attendees']

        widgets = {
        'booking_date': forms.DateInput(
            format=('%Y-%m-%d'),
            attrs={'class': 'form-control', 
                'placeholder': 'Select a date',
                'type': 'date'
                }),
            'booking_time': forms.TimeInput(
            format=('%H:%M'),
            attrs={'class': 'form-control', 
                'placeholder': 'Select a time',
                'type': 'time'
                }),
        }
