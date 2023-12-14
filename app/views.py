from django.shortcuts import render, redirect

from .models import Shape

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def home(request):
    shapes = Shape.objects.all()
    return render(request, 'home.html', {'shapes': shapes})

def about(request):
    return render(request, 'about.html', {})

def design(request):
    return render(request, 'design.html', {})

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ("Login successful"))
            return redirect('home')
        else:
            messages.success(request, ("Error logging in"))
            return redirect('login')
    else:
        return render(request, 'login.html', {})

        
    
    
def logout_user(request):
    logout(request)
    messages.success(request, ("Logout success"))
    return redirect('home')

