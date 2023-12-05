from django.shortcuts import render
from .models import Shape


def home(request):
    shapes = Shape.objects.all()
    return render(request, 'home.html', {'shapes': shapes})
