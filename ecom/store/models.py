from django.db import models
from django.contrib.auth.models import User

# Category model to represent different product categories (e.g., Electronics, Clothing)
class Category(models.Model):
    # Name of the category (e.g., 'Electronics', 'Clothing')
    name = models.CharField(max_length=100)

    # Description of the category (optional field)
    description = models.TextField(blank=True)

    # Image associated with the category (uploaded to 'categories/' directory)
    image = models.ImageField(upload_to='categories/', blank=True, null=True)

    # String representation of the Category, using the name
    def __str__(self):
        return self.name

# Product model representing individual products in the store
class Products(models.Model):
    # Name of the product (e.g., 'Smartphone', 'T-Shirt')
    name = models.CharField(max_length=200)

    # Detailed description of the product
    description = models.TextField()

    # Price of the product (using Decimal for accuracy in financial values)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    # Price of the product in INR (Indian Rupees)
    price_inr = models.DecimalField(max_digits=10, decimal_places=2)

    # Image representing the product (uploaded to 'products/' directory)
    image = models.ImageField(upload_to='products/')

    # ForeignKey linking the product to a specific category (one-to-many relationship)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    # Quantity of the product available in stock
    stock = models.PositiveIntegerField(default=0)

    # Timestamps for when the product is created and last updated
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # String representation of the product, using the name
    def __str__(self):
        return self.name

# Profile model for storing additional user information (such as address and phone number)
class Profile(models.Model):
    # One-to-one relationship with the User model (Django's built-in authentication system)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Shipping address for the user (optional field)
    address = models.TextField(blank=True)

    # User's phone number (optional field)
    phone_number = models.CharField(max_length=15, blank=True)

    # Profile picture (uploaded to 'profile_pics/' directory), with a default image if not uploaded
    profile_picture = models.ImageField(upload_to='profile_pics/', default='default.jpg')

    # String representation of the Profile, showing the user's username
    def __str__(self):
        return f"{self.user.username}'s Profile"

# Order model to represent customer orders
class Order(models.Model):
    # Status choices for an order (e.g., 'pending', 'shipped', 'delivered')
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('processing', 'Processing'),
        ('shipped', 'Shipped'),
        ('delivered', 'Delivered'),
        ('cancelled', 'Cancelled'),
    )

    # ForeignKey linking the order to a user (one-to-many relationship with the User model)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # Unique order number for each order
    order_number = models.CharField(max_length=20, unique=True)

    # Date and time when the order was placed
    order_date = models.DateTimeField(auto_now_add=True)

    # Status of the order (using predefined STATUS_CHOICES)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')

    # Total amount for the order
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    # Shipping address for the order
    shipping_address = models.TextField()

    # Phone number of the customer for order contact
    phone_number = models.CharField(max_length=15)

    # Email of the customer (optional)
    email = models.EmailField(null=True, blank=True)

    # String representation of the order, showing the order number
    def __str__(self):
        return f"Order {self.order_number}"

# OrderItem model to represent each item within an order
class OrderItem(models.Model):
    # ForeignKey linking the order item to a specific order
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')

    # ForeignKey linking the order item to a specific product
    product = models.ForeignKey(Products, on_delete=models.CASCADE)

    # Quantity of the product in the order
    quantity = models.PositiveIntegerField()

    # Price of the product at the time of the order
    price = models.DecimalField(max_digits=10, decimal_places=2)

    # String representation of the order item, showing quantity and product name
    def __str__(self):
        return f"{self.quantity} x {self.product.name}"

    # Property method to calculate the subtotal for this order item (quantity * price)
    @property
    def subtotal(self):
        return self.quantity * self.price
