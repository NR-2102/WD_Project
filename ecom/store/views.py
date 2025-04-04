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
        email = request.POST.get('email')  # email from the POST request
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)  # email as the username
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
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password_check = request.POST.get('password-check')
        
        if password != password_check:
            messages.error(request, 'Passwords do not match')
            return redirect('register')
            
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists')
            return redirect('register')
            
        try:
            user = User.objects.create_user(
                username=email,  # Using email as username
                email=email,
                password=password,
                first_name=name
            )
            messages.success(request, 'You have been registered successfully')
            return redirect('login')
        except Exception as e:
            messages.error(request, f'Error creating account: {str(e)}')
            return redirect('register')
    else:
        return render(request, 'register.html', {})