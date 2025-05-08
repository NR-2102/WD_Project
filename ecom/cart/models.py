from django.db import models
from django.contrib.auth.models import User
from store.models import Products  # Import the Products model from the store app


# Cart model to represent a user's shopping cart
class Cart(models.Model):
    # Associate a cart with a user (optional, for guest users user can be null)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    
    # Automatically set the timestamp when the cart is created
    created_at = models.DateTimeField(auto_now_add=True)
    
    # Automatically update the timestamp when the cart is modified
    updated_at = models.DateTimeField(auto_now=True)

    # String representation for admin or debugging
    def __str__(self):
        return f"Cart {self.id}"

    # Calculate the total price of all items in the cart
    def get_total_price(self):
        total = 0
        for item in self.items.all():  # 'items' is the related_name from CartItem
            total += item.get_total_price()
        return total

    # Calculate the total quantity of items in the cart
    def get_total_items(self):
        total = 0
        for item in self.items.all():
            total += item.quantity
        return total


# CartItem model represents a product entry in a cart
class CartItem(models.Model):
    # Link each cart item to a specific cart
    cart = models.ForeignKey(Cart, related_name='items', on_delete=models.CASCADE)

    # Link to the actual product being added
    product = models.ForeignKey(Products, on_delete=models.CASCADE)

    # Quantity of the product in the cart
    quantity = models.PositiveIntegerField(default=1)

    # Timestamp for when this item was added
    created_at = models.DateTimeField(auto_now_add=True)

    # Timestamp for when this item was last updated
    updated_at = models.DateTimeField(auto_now=True)

    # String representation for admin or debugging
    def __str__(self):
        return f"{self.quantity} x {self.product.name}"

    # Calculate the total price for this item (quantity * product price)
    def get_total_price(self):
        return self.quantity * self.product.price_inr
