from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.index, name='home'),
    #path('register/', views.register, name='register'),
]