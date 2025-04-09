from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Book, UserLibrary, UserProfile
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .forms import CustomUserCreationForm, CustomAuthenticationForm, UserProfileForm
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
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                # Create the user
                user = form.save(commit=False)
                user.email = form.cleaned_data.get('email')
                user.first_name = form.cleaned_data.get('first_name')
                user.last_name = form.cleaned_data.get('last_name')
                user.save()
                
                # Get or create the user profile
                profile, created = UserProfile.objects.get_or_create(user=user)
                
                # Update profile with additional information
                profile.birth_date = form.cleaned_data.get('birth_date')
                profile.gender = form.cleaned_data.get('gender')
                profile.phone_number = form.cleaned_data.get('phone_number')
                profile.address = form.cleaned_data.get('address')
                profile.bio = form.cleaned_data.get('bio')
                
                # Handle profile picture
                if 'profile_picture' in request.FILES:
                    profile.profile_picture = request.FILES['profile_picture']
                
                profile.save()
                
                # Log the user in
                login(request, user)
                messages.success(request, 'Account created successfully! Welcome to Kindle Clone.')
                return redirect('home')
            except Exception as e:
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
                messages.success(request, f'Welcome back, {user.first_name}!')
                return redirect('home')
            else:
                messages.error(request, 'Invalid username or password.')
    else:
        form = CustomAuthenticationForm()
    
    return render(request, 'registration/login.html', {'form': form})

@login_required
def my_library(request):
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
    return redirect('my_library')

@login_required
def remove_from_library(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    # Get the user's library
    library = get_object_or_404(UserLibrary, user=request.user)
    # Remove the book from the library
    library.books.remove(book)
    messages.success(request, f'"{book.title}" has been removed from your library.')
    return redirect('my_library')

@login_required
def profile(request):
    user = request.user
    profile, created = UserProfile.objects.get_or_create(user=user)
    
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated successfully!')
            return redirect('profile')
    else:
        form = UserProfileForm(instance=profile)
    
    return render(request, 'books/profile.html', {
        'form': form,
        'profile': profile,
        'user': user
    })

# Custom logout view
def logout_view(request):
    logout(request)
    messages.info(request, 'You have been logged out successfully.')
    return redirect('home')

# Signal to create UserLibrary for new users
@receiver(post_save, sender=User)
def create_user_library(sender, instance, created, **kwargs):
    if created:
        UserLibrary.objects.create(user=instance)
