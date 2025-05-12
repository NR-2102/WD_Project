from django.db import models # 	To use Django's model fields and features
from django.contrib.auth.models import User # To use Django's built-in user accounts

# CharField(max_length=200) = stores the 'short text string'..
# TextField() = store the long 'strings' or 'characters'..
# OneToOneField = single profile to single user..
# ForeignKey = many profiles to single user..
# ManyToManyField = many profiles to many users..
# ImageField = Stores image files..
# PositiveIntegerField = store only non-negative integers..
# DateTimeField = store both date and time in one field..
# EmailField =  store email addresses..

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self): # __str__ = magic method
        return self.name

class Products(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2) 
    price_inr = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/')
    # on_delete=models.CASCADE = Delete this object if its category is deleted
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    stock = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True) # (auto_now_add=True) =  Automatically set the value when the object is created
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.TextField(blank=True) # TextField store the long 'strings' or 'characters'.. 
    phone_number = models.CharField(max_length=15, blank=True) # CharField stores the 'short text string'..
    profile_picture = models.ImageField(upload_to='profile_pics/', default='default.jpg')

    def __str__(self):
        return f"{self.user.username}'s Profile"

class Order(models.Model):
    STATUS_CHOICES = ( # (p, P) --> (p = store in database); (P = show on site)
        ('pending', 'Pending'),
        ('processing', 'Processing'),
        ('shipped', 'Shipped'),
        ('delivered', 'Delivered'),
        ('cancelled', 'Cancelled'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order_number = models.CharField(max_length=20, unique=True)
    order_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    shipping_address = models.TextField()
    phone_number = models.CharField(max_length=15)
    email = models.EmailField(null=True, blank=True)

    def __str__(self):
        return f"Order {self.order_number}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"

    @property
    def subtotal(self):
        return self.quantity * self.price
