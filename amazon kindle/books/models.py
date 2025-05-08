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
    book_file = models.FileField(upload_to='book_files/', null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='OTHER')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

class UserLibrary(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    books = models.ManyToManyField(Book, blank=True)
    
    def __str__(self):
        return f"{self.user.username}'s Library"

@receiver(post_save, sender=User)
def create_user_library(sender, instance, created, **kwargs):
    if created:
        UserLibrary.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_library(sender, instance, **kwargs):
    instance.userlibrary.save()




