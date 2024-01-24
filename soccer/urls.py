from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.index, name='home'),
    path('accounts/signup', views.account, name='register'),
    path('profile/', views.profile, name='profile'),
   # path('register/', views.register, name='register'),
]