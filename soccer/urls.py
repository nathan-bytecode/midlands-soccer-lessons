from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.index, name='home'),
    path('account/', views.account, name='account'),

]