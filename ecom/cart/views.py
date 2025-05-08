from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from store.models import Products
from .models import Cart, CartItem

# Get or create a cart for the current user or session
def get_or_create_cart(request):
    # If user is logged in, get or create a Cart associated with the user
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user)
    else:
        # For anonymous users, use session to store cart_id
        cart_id = request.session.get('cart_id')
        if cart_id:
            cart = Cart.objects.get(id=cart_id)
        else:
            # If no cart exists in session, create a new one and store its ID in the session
            cart = Cart.objects.create()
            request.session['cart_id'] = cart.id
    return cart

# Show the cart page with cart details and items
def cart_summary(request):
    cart = get_or_create_cart(request)
    items = cart.items.all()  # Get all items using the related_name from CartItem model
    return render(request, 'cart_summary.html', {
        'cart': cart,
        'items': items,
        'total_price': cart.get_total_price(),
        'total_items': cart.get_total_items()
    })

# Add a product to the cart
def cart_add(request):
    if request.method == 'POST':
        # Get product ID and quantity from the POST request
        product_id = request.POST.get('product_id')
        quantity = int(request.POST.get('quantity', 1))  # Default quantity is 1

        # Retrieve the product or return 404 if not found
        product = get_object_or_404(Products, id=product_id)

        # Get or create the cart
        cart = get_or_create_cart(request)

        # Get or create the CartItem; if it already exists, increase the quantity
        item, created = CartItem.objects.get_or_create(
            cart=cart, product=product,
            defaults={'quantity': quantity}
        )

        if not created:
            item.quantity += quantity
            item.save()

        # Display success message
        messages.success(request, f'{product.name} added to cart!')
    return redirect('cart_summary')

# Remove a product from the cart
def cart_delete(request):
    if request.method == 'POST':
        # Get the item ID from the POST data
        item_id = request.POST.get('item_id')

        # Get the cart
        cart = get_or_create_cart(request)

        # Get the specific CartItem or raise 404 if not found
        item = get_object_or_404(CartItem, id=item_id, cart=cart)

        # Delete the item from the cart
        item.delete()

        # Show confirmation message
        messages.success(request, 'Item removed from cart.')
    return redirect('cart_summary')

# Update the quantity of an item in the cart
def cart_update(request):
    if request.method == 'POST':
        # Get item ID and new quantity from POST data
        item_id = request.POST.get('item_id')
        quantity = int(request.POST.get('quantity', 1))

        # Get the cart
        cart = get_or_create_cart(request)

        # Retrieve the specific CartItem
        item = get_object_or_404(CartItem, id=item_id, cart=cart)

        # Update the quantity and save
        item.quantity = quantity
        item.save()

        # Show update message
        messages.success(request, 'Cart updated.')
    return redirect('cart_summary')
