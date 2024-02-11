from django.contrib import admin
from .models import Account, Course1, Course2, Course3, Booking

class BookingAdmin(admin.ModelAdmin):
    list_display = (
        'booking_date',
        'booking_time',
    )
# Register your models here.
admin.site.register(Account)
admin.site.register(Course1)
admin.site.register(Course2)
admin.site.register(Course3)
admin.site.register(Booking, BookingAdmin)


