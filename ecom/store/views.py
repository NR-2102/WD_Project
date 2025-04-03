from django.shortcuts import render, redirect
from .models import Products
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

# Create your views here.
def home(request):
    products = Products.objects.all()
    return render(request, 'home.html', {'products': products})

def deals(request):
    return render(request, 'deals.html', {})

def login_user(request):
    if request.method == 'POST':
        email = request.POST.get('email')  # Get email from the POST request
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)  # Use email as the username
        if user is not None:
            login(request, user)
            messages.success(request, 'You have been logged in successfully')
            return redirect('home')
        else:
            messages.error(request, 'Invalid email or password')
            return redirect('login')
    else:
        return render(request, 'login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, 'You have been logged out successfully')
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)  # Use UserCreationForm
        if form.is_valid():
            user = form.save()  # Create and save the user
            messages.success(request, 'You have been registered successfully')
            return redirect('login')
        else:
            for error_list in form.errors.values():
                for error in error_list:
                    messages.error(request, error)
            return render(request, 'register.html', {'form': form})
    else:
        form = UserCreationForm()  # Create an empty form for GET requests
        return render(request, 'register.html', {'form': form})