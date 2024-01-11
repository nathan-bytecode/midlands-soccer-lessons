from . import views
from django.urls import path

urlpatterns = [
    path('', views.Account, name='account'),
]