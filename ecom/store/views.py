from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Products, Category, Profile, Order, OrderItem
from django.contrib.auth.models import User
from decimal import Decimal
from cart.views import get_or_create_cart
import uuid
from datetime import datetime
from django.db.models import Q


def home(request):
    search_query = request.GET.get('q', '')
    if search_query:
        products = Products.objects.filter(
            Q(name__icontains=search_query) |
            Q(description__icontains=search_query) |
            Q(category__name__icontains=search_query)
        ).distinct()
    else:
        products = Products.objects.all()
    return render(request, 'home.html', {'products': products, 'search_query': search_query})

def login_user(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        # Try to authenticate with email first
        try:
            user = User.objects.get(email=email)
            user = authenticate(request, username=user.username, password=password)
        except User.DoesNotExist:
            # If email not found, try username
            user = authenticate(request, username=email, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, 'You have been logged in successfully')
            return redirect('home')
        else:
            messages.error(request, 'Invalid email/username or password')
            return redirect('login')
    else:
        return render(request, 'login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, 'Successfully logged out!')
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        
        if password != confirm_password:
            messages.error(request, 'Passwords do not match')
            return redirect('register')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists')
            return redirect('register')
        
        username = email.split('@')[0]
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name
        )
        
        Profile.objects.create(user=user)
        
        messages.success(request, 'Account created successfully! Please login.')
        return redirect('login')
        
    return render(request, 'register.html')

def product_description(request, pk):
    product = get_object_or_404(Products, id=pk)
    related_products = Products.objects.filter(category=product.category).exclude(id=pk)[:4]
    return render(request, 'product_description.html', {
        'product': product,
        'related_products': related_products
    })

def category_name(request, category_name):
    category = get_object_or_404(Category, name=category_name)
    products = Products.objects.filter(category=category)
    
    # Create a context dictionary with the category and products
    context = {
        'category': category,
        'category_name': category_name,
        'products': products
    }
    
    return render(request, 'category.html', context)

@login_required
def profile(request):
    if request.method == 'POST':
        user = request.user
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.email = request.POST.get('email')
        user.save()
        
        profile = user.profile
        profile.phone_number = request.POST.get('phone_number')
        profile.address = request.POST.get('address')
        
        if 'profile_picture' in request.FILES:
            profile.profile_picture = request.FILES['profile_picture']
        
        profile.save()
        
        messages.success(request, 'Profile updated successfully!')
        return redirect('profile')
    
    return render(request, 'profile.html')

@login_required
def change_password(request):
    if request.method == 'POST':
        current_password = request.POST.get('current_password')
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')
        
        if not request.user.check_password(current_password):
            messages.error(request, 'Current password is incorrect')
            return redirect('profile')
        
        if new_password != confirm_password:
            messages.error(request, 'New passwords do not match')
            return redirect('profile')
        
        if len(new_password) < 8:
            messages.error(request, 'Password must be at least 8 characters long')
            return redirect('profile')
        
        request.user.set_password(new_password)
        request.user.save()
        
        update_session_auth_hash(request, request.user)
        
        messages.success(request, 'Password changed successfully')
        return redirect('profile')
    
    return redirect('profile')

@login_required
def cart_summary(request):
    cart = request.session.get('cart', {})
    items = []
    total = Decimal('0.00')
    
    for product_id, quantity in cart.items():
        product = get_object_or_404(Products, id=product_id)
        item_total = product.price * quantity
        total += item_total
        items.append({
            'product': product,
            'quantity': quantity,
            'subtotal': item_total
        })
    
    return render(request, 'cart.html', {
        'items': items,
        'total': total
    })

@login_required
def checkout(request):
    cart = get_or_create_cart(request)
    if not cart or not cart.items.exists():
        messages.error(request, 'Your cart is empty')
        return redirect('cart_summary')

    items = cart.items.all()
    total_price = cart.get_total_price()

    if request.method == 'POST':
        try:
            # Generate unique order number
            order_number = f"ORD-{datetime.now().strftime('%Y%m%d')}-{str(uuid.uuid4())[:8]}"
            
            # Create order
            order = Order.objects.create(
                user=request.user,
                order_number=order_number,
                total_amount=total_price,
                shipping_address=request.POST.get('shipping_address'),
                phone_number=request.POST.get('phone_number'),
                email=request.POST.get('email')
            )

            # Create order items
            for item in items:
                OrderItem.objects.create(
                    order=order,
                    product=item.product,
                    quantity=item.quantity,
                    price=item.product.price_inr
                )

            # Clear cart
            cart.items.all().delete()
            
            messages.success(request, f'Order placed successfully! Order number: {order_number}')
            return redirect('order_confirmation', order_number=order_number)
            
        except Exception as e:
            messages.error(request, f'Error processing order: {str(e)}')
            return redirect('checkout')

    return render(request, 'checkout.html', {
        'items': items,
        'total_price': total_price,
        'user': request.user
    })

@login_required
def order_confirmation(request, order_number):
    order = get_object_or_404(Order, order_number=order_number, user=request.user)
    return render(request, 'order_confirmation.html', {'order': order})

@login_required
def order_history(request):
    orders = Order.objects.filter(user=request.user).order_by('-order_date')
    return render(request, 'order_history.html', {'orders': orders})

def search_results(request):
    search_query = request.GET.get('q', '')
    if search_query:
        products = Products.objects.filter(
            Q(name__icontains=search_query) |
            Q(description__icontains=search_query) |
            Q(category__name__icontains=search_query)
        ).distinct()
    else:
        products = Products.objects.none()
    
    categories = Category.objects.all()
    
    return render(request, 'search_results.html', {
        'products': products,
        'search_query': search_query,
        'categories': categories
    })
