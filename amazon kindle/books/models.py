from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Book(models.Model):
    CATEGORY_CHOICES = (
        ('FICTION', 'Fiction'),
        ('NONFICTION', 'Non-Fiction'),
        ('SCIENCE', 'Science'),
        ('HISTORY', 'History'),
        ('BUSINESS', 'Business'),
        ('TECHNOLOGY', 'Technology'),
        ('BIOGRAPHY', 'Biography'),
        ('CHILDREN', 'Children'),
        ('POETRY', 'Poetry'),
        ('OTHER', 'Other'),
    )
    
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    description = models.TextField()
    cover_image = models.ImageField(upload_to='book_covers/', null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='OTHER')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

class UserProfile(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(max_length=500, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True)
    phone_number = models.CharField(max_length=15, blank=True)
    address = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.user.username}'s Profile"

class UserLibrary(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    books = models.ManyToManyField(Book, blank=True)
    
    def __str__(self):
        return f"{self.user.username}'s Library"

# Signal to create UserProfile and UserLibrary for new users
@receiver(post_save, sender=User)
def create_user_profile_and_library(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
        UserLibrary.objects.create(user=instance)
