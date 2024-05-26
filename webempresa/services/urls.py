from django.urls import path
from .import views

urlpatterns = [
    #Paths de services
    path('', views.services, name='services'),
]