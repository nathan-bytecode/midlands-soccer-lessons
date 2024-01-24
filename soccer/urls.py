from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.index, name='home'),
    path('accounts/signup', views.account, name='register'),
    path('profile/', views.profile, name='profile'),
    path('courses/', views.courses, name='courses'),
    path('bookings/', views.bookings, name='bookings'),
   # path('register/', views.register, name='register'),
]