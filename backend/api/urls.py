from django.urls import path
from .views import main

#Main urls
urlpatterns = [
    #matches path to the functions in views.py
    path('home', main)
]