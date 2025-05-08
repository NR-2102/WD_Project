# Import necessary Django model classes
from django.db import models
from django.contrib.auth.models import User
from store.models import Products  # Import Products model from store app

# Model to represent a shopping cart
class Cart(models.Model):
    # Optional reference to a user (null and blank allowed for anonymous carts)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    # Timestamp for when the cart was created
    created_at = models.DateTimeField(auto_now_add=True)
    # Timestamp for when the cart was last updated
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        # String representation of the cart (e.g., "Cart 1")
        return f"Cart {self.id}"

    # Method to calculate total price of all items in the cart
    def get_total_price(self):
        total = 0
        # Sum the total price of each cart item
        for item in self.items.all():
            total += item.get_total_price()
        return total

    # Method to calculate total number of items in the cart
    def get_total_items(self):
        total = 0
        # Sum the quantity of each cart item
        for item in self.items.all():
            total += item.quantity
        return total

# Model to represent a single item in a cart
class CartItem(models.Model):
    # Each item is linked to a cart; `related_name='items'` allows accessing items via cart.items
    cart = models.ForeignKey(Cart, related_name='items', on_delete=models.CASCADE)
    # Each item is associated with a specific product
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    # Quantity of the product in the cart
    quantity = models.PositiveIntegerField(default=1)
    # Timestamp for when the item was added
    created_at = models.DateTimeField(auto_now_add=True)
    # Timestamp for when the item was last updated
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        # String representation (e.g., "2 x iPhone 13")
        return f"{self.quantity} x {self.product.name}"

    # Method to calculate total price for this cart item
    def get_total_price(self):
        return self.quantity * self.product.price_inr
