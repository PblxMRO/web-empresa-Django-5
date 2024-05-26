from django.urls import path
from .import views

urlpatterns = [
    #Paths de contact
    path('', views.contact, name='contact'),
   
]