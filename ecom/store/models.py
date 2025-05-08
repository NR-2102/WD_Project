from django.db import models
from django.contrib.auth.models import User

# Category model to define product categories like "Electronics" or "Clothing"
class Category(models.Model):
    name = models.CharField(max_length=100)  # The name of the category (e.g., Electronics)
    description = models.TextField(blank=True)  # An optional description of the category
    image = models.ImageField(upload_to='categories/', blank=True, null=True)  # Optional image for the category

    def __str__(self):
        return self.name  # Returns the name of the category when printed


# Products model to define individual products in the store
class Products(models.Model):
    name = models.CharField(max_length=200)  # The name of the product
    description = models.TextField()  # Detailed description of the product
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Price of the product in default currency
    price_inr = models.DecimalField(max_digits=10, decimal_places=2)  # Price of the product in INR (Indian Rupees)
    image = models.ImageField(upload_to='products/')  # Product image
    category = models.ForeignKey(Category, on_delete=models.CASCADE)  # Linking the product to a category
    stock = models.PositiveIntegerField(default=0)  # Stock availability of the product
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set when the product is created
    updated_at = models.DateTimeField(auto_now=True)  # Automatically set when the product is updated

    def __str__(self):
        return self.name  # Returns the name of the product when printed


# Profile model to store additional user details (One-to-One relationship with User model)
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # A one-to-one relationship with the User model
    address = models.TextField(blank=True)  # Optional address field for the user
    phone_number = models.CharField(max_length=15, blank=True)  # Optional phone number for the user
    profile_picture = models.ImageField(upload_to='profile_pics/', default='default.jpg')  # Profile picture with default image

    def __str__(self):
        return f"{self.user.username}'s Profile"  # Returns a string representation of the profile


# Order model to represent an order placed by a user
class Order(models.Model):
    # Choices for the order status
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('processing', 'Processing'),
        ('shipped', 'Shipped'),
        ('delivered', 'Delivered'),
        ('cancelled', 'Cancelled'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Linking the order to the user who placed it
    order_number = models.CharField(max_length=20, unique=True)  # Unique order number for each order
    order_date = models.DateTimeField(auto_now_add=True)  # Automatically set when the order is placed
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')  # Status of the order
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)  # Total amount of the order
    shipping_address = models.TextField()  # Shipping address for the order
    phone_number = models.CharField(max_length=15)  # Phone number associated with the order
    email = models.EmailField(null=True, blank=True)  # Optional email field for the user

    def __str__(self):
        return f"Order {self.order_number}"  # Returns a string representation of the order


# OrderItem model to represent individual products in an order
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')  # Linking the order to the order item
    product = models.ForeignKey(Products, on_delete=models.CASCADE)  # Linking the product to the order item
    quantity = models.PositiveIntegerField()  # Quantity of the product in the order
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Price of the product at the time of the order

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"  # Returns a string representation of the order item

    # Property to calculate the subtotal for the order item (quantity * price)
    @property
    def subtotal(self):
        return self.quantity * self.price
