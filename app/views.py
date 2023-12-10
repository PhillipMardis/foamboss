from django.shortcuts import render
from .models import Shape


def home(request):
    shapes = Shape.objects.all()
    return render(request, 'home.html', {'shapes': shapes})

def about(request):
    return render(request, 'about.html', {})

def design(request):
    return render(request, 'design.html', {})