# Import necessary Django utilities and models
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from store.models import Products
from .models import Cart, CartItem

# Utility function to get or create a cart for the current user or session
def get_or_create_cart(request):
    if request.user.is_authenticated:
        # Logged-in users: get or create a cart linked to the user
        cart, created = Cart.objects.get_or_create(user=request.user)
    else:
        # Anonymous users: manage cart using session
        cart_id = request.session.get('cart_id')
        if cart_id:
            # Try to get existing cart using cart_id from session
            cart = Cart.objects.get(id=cart_id)
        else:
            # If not found, create a new cart and store its ID in the session
            cart = Cart.objects.create()
            request.session['cart_id'] = cart.id
    return cart

# View to display the cart summary page
def cart_summary(request):
    # Get or create the cart
    cart = get_or_create_cart(request)
    # Retrieve all items in the cart (using related_name='items')
    items = cart.items.all()
    # Render the cart summary template with cart details
    return render(request, 'cart_summary.html', {
        'cart': cart,
        'items': items,
        'total_price': cart.get_total_price(),
        'total_items': cart.get_total_items()
    })

# View to handle adding a product to the cart
def cart_add(request):
    if request.method == 'POST':
        # Get the product ID and desired quantity from the POST request
        product_id = request.POST.get('product_id')
        quantity = int(request.POST.get('quantity', 1))

        # Fetch the product from the database or return 404 if not found
        product = get_object_or_404(Products, id=product_id)
        # Get or create the user's/session's cart
        cart = get_or_create_cart(request)

        # Get or create a CartItem for the product
        item, created = CartItem.objects.get_or_create(
            cart=cart, product=product,
            defaults={'quantity': quantity}
        )

        # If the item already exists, update the quantity
        if not created:
            item.quantity += quantity
            item.save()

        # Display a success message
        messages.success(request, f'{product.name} added to cart!')
    # Redirect to the cart summary page
    return redirect('cart_summary')

# View to handle deleting an item from the cart
def cart_delete(request):
    if request.method == 'POST':
        # Get the item ID from the POST request
        item_id = request.POST.get('item_id')
        # Get the user's/session's cart
        cart = get_or_create_cart(request)
        # Fetch the CartItem or return 404 if not found
        item = get_object_or_404(CartItem, id=item_id, cart=cart)
        # Delete the item from the cart
        item.delete()
        # Display a success message
        messages.success(request, 'Item removed from cart.')
    # Redirect to the cart summary page
    return redirect('cart_summary')

# View to handle updating the quantity of a cart item
def cart_update(request):
    if request.method == 'POST':
        # Get item ID and new quantity from POST request
        item_id = request.POST.get('item_id')
        quantity = int(request.POST.get('quantity', 1))

        # Get the user's/session's cart
        cart = get_or_create_cart(request)
        # Fetch the CartItem or return 404 if not found
        item = get_object_or_404(CartItem, id=item_id, cart=cart)
        # Update the item's quantity and save it
        item.quantity = quantity
        item.save()
        # Display a success message
        messages.success(request, 'Cart updated.')
    # Redirect to the cart summary page
    return redirect('cart_summary')
