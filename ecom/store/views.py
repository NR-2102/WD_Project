from django.shortcuts import render, redirect, get_object_or_404
from .models import Products
from .models import Category
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
                username=email,  
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

def product_description(request, pk):
    product = get_object_or_404(Products, id=pk)
    
    # Convert price to rupees
    exchange_rate = 83  # 1 USD = 83 INR (approx)
    product.price_inr = float(product.price) * exchange_rate
    
    # Get related products from the same category
    related_products = Products.objects.filter(category=product.category).exclude(id=pk)[:4]
    
    # Convert prices for related products
    for related in related_products:
        related.price_inr = float(related.price) * exchange_rate
    
    category_name = product.category.name
    
    # Prepare specifications based on category
    specs = []
    
    if category_name == 'Electronics':
        specs = [
            {'name': 'Brand', 'value': product.brand or 'N/A'},
            {'name': 'Model Number', 'value': product.model_number or 'N/A'},
            {'name': 'Warranty', 'value': product.warranty or 'N/A'},
        ]
    
    elif category_name == 'Sports':
        specs = [
            {'name': 'Brand', 'value': product.brand or 'N/A'},
            {'name': 'Material', 'value': product.get_attribute('material') or 'N/A'},
            {'name': 'Suitable For', 'value': product.get_attribute('suitable_for') or 'N/A'},
        ]
    
    elif category_name == 'Fashion':
        specs = [
            {'name': 'Brand', 'value': product.brand or 'N/A'},
            {'name': 'Material', 'value': product.get_attribute('material') or 'N/A'},
            {'name': 'Size', 'value': product.get_attribute('size') or 'N/A'},
            {'name': 'Color', 'value': product.get_attribute('color') or 'N/A'},
        ]
    
    elif category_name == 'Beauty & Personal Care':
        specs = [
            {'name': 'Brand', 'value': product.brand or 'N/A'},
            {'name': 'Skin Type', 'value': product.get_attribute('skin_type') or 'N/A'},
            {'name': 'Ingredients', 'value': product.get_attribute('ingredients') or 'N/A'},
        ]
    
    context = {
        'product': product,
        'category_name': category_name,
        'related_products': related_products,
        'specifications': specs,
    }
    
    return render(request, 'product_description.html', context)
    
