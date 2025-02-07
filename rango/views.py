from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("Rango says hey there partner!")

def about(request):
    return HttpResponse("Rango says this is the about page!")
