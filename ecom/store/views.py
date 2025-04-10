from django.shortcuts import render, redirect, get_object_or_404
from .models import Products
from .models import Category
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .forms import UserRegistrationForm, LoginForm


# Create your views here.
def home(request):
    products = Products.objects.all()
    for product in products:
        product.price_inr = product.price_inr  # This line is just to ensure the price_inr is available in the template
    return render(request, 'home.html', {'products': products})

def deals(request):
    return render(request, 'deals.html')

def login_user(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
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
    
    # Get related products from the same category
    related_products = Products.objects.filter(category=product.category).exclude(id=pk)[:4]
    
    # Get category name
    category_name = product.category.name
    
    # Prepare specifications based on category
    specs = []
    
    if category_name == 'Electronics':
        specs = [
            {'name': 'Brand', 'value': product.brand or 'N/A'},
            {'name': 'Model Number', 'value': getattr(product, 'model_number', 'N/A')},
            {'name': 'Warranty', 'value': getattr(product, 'warranty', 'N/A')},
        ]
    
    elif category_name == 'Sports':
        specs = [
            {'name': 'Brand', 'value': product.brand or 'N/A'},
            {'name': 'Description', 'value': product.description or 'N/A'},
            {'name': 'Features', 'value': getattr(product, 'feature', 'N/A')},
        ]
    
    elif category_name == 'Fashion':
        specs = [
            {'name': 'Brand', 'value': product.brand or 'N/A'},
            {'name': 'Description', 'value': product.description or 'N/A'},
            {'name': 'Features', 'value': getattr(product, 'feature', 'N/A')},
        ]
    
    elif category_name == 'Beauty & Personal Care':
        specs = [
            {'name': 'Brand', 'value': product.brand or 'N/A'},
            {'name': 'Description', 'value': product.description or 'N/A'},
            {'name': 'Features', 'value': getattr(product, 'feature', 'N/A')},
        ]
    
    context = {
        'product': product,
        'category_name': category_name,
        'related_products': related_products,
        'specifications': specs,
    }
    
    return render(request, 'product_description.html', context)
    
def category_name(request, category_name):
    try:
        category = Category.objects.get(name=category_name)
        products = Products.objects.filter(category=category)
        
        if not products.exists():
            messages.info(request, f'No products found in the {category_name} category.')
        
        context = {
            'category_name': category_name,
            'products': products
        }
        return render(request, 'category.html', context)
    except Category.DoesNotExist:
        messages.error(request, f'Category "{category_name}" does not exist.')
        return redirect('home')
    
def category(request, category_name):
    # Get the category object
    category_obj = get_object_or_404(Category, name=category_name)
    
    # Get all products in this category
    products = Products.objects.filter(category=category_obj)
    
    context = {
        'category_name': category_name,
        'products': products,
    }
    
    return render(request, 'category.html', context)

def cart(request):
    return render(request, 'cart.html', {})
    
