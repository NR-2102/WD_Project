from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Book, UserLibrary
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.utils import timezone

def home(request):
    category = request.GET.get('category', '')
    if category:
        books = Book.objects.filter(category=category)
    else:
        books = Book.objects.all()
    
    categories = Book.CATEGORY_CHOICES
    return render(request, 'books/home.html', {
        'books': books,
        'categories': categories,
        'selected_category': category
    })

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            try:
                # Create the user
                user = form.save(commit=False)
                user.email = form.cleaned_data.get('email')
                user.save()
                
                # Log the user in
                login(request, user)
                messages.success(request, 'Account created successfully! Welcome to Kindle Clone.')
                return redirect('home')
            except Exception as e:
                # If there's an error, delete the user if it was created
                if user and user.id:
                    user.delete()
                messages.error(request, f'Error creating account: {str(e)}')
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'books/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                if user.first_name:
                    messages.success(request, f'Welcome back, {user.first_name}!')
                else:
                    messages.success(request, f'Welcome back, {user.username}!')
                return redirect('home')
            else:
                messages.error(request, 'Invalid username or password.')
    else:
        form = CustomAuthenticationForm()
    
    return render(request, 'registration/login.html', {'form': form})

@login_required
def library(request):
    # Get or create UserLibrary for the current user
    library, created = UserLibrary.objects.get_or_create(user=request.user)
    return render(request, 'books/library.html', {'library': library})

@login_required
def add_to_library(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    # Get or create UserLibrary for the current user
    library, created = UserLibrary.objects.get_or_create(user=request.user)
    library.books.add(book)
    messages.success(request, f'"{book.title}" has been added to your library.')
    return redirect('library')

@login_required
def remove_from_library(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    # Get or create UserLibrary for the current user
    library, created = UserLibrary.objects.get_or_create(user=request.user)
    # Remove the book from the library
    library.books.remove(book)
    messages.success(request, f'"{book.title}" has been removed from your library.')
    return redirect('library')

# Custom logout view
def logout_view(request):
    logout(request)
    messages.info(request, 'You have been logged out successfully.')
    return redirect('home')

@login_required
def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    # Get or create UserLibrary for the current user
    library, created = UserLibrary.objects.get_or_create(user=request.user)
    is_in_library = book in library.books.all()
    
    return render(request, 'books/book_detail.html', {
        'book': book,
        'is_in_library': is_in_library
    })
