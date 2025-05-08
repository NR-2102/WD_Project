from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from store.models import Products
from .models import Cart, CartItem

# Get or create a cart for the current user or session
def get_or_create_cart(request):
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user)
    else:
        cart_id = request.session.get('cart_id')
        if cart_id:
            cart = Cart.objects.get(id=cart_id)
        else:
            cart = Cart.objects.create()
            request.session['cart_id'] = cart.id
    return cart

# Show the cart page
def cart_summary(request):
    cart = get_or_create_cart(request)
    items = cart.items.all()  # cart.items is related_name in CartItem model
    return render(request, 'cart_summary.html', {
        'cart': cart,
        'items': items,
        'total_price': cart.get_total_price(),
        'total_items': cart.get_total_items()
    })

# Add a product to the cart
def cart_add(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        quantity = int(request.POST.get('quantity', 1))

        product = get_object_or_404(Products, id=product_id)
        cart = get_or_create_cart(request)

        item, created = CartItem.objects.get_or_create(
            cart=cart, product=product,
            defaults={'quantity': quantity}
        )

        if not created:
            item.quantity += quantity
            item.save()

        messages.success(request, f'{product.name} added to cart!')
    return redirect('cart_summary')

# Remove a product from the cart
def cart_delete(request):
    if request.method == 'POST':
        item_id = request.POST.get('item_id')
        cart = get_or_create_cart(request)
        item = get_object_or_404(CartItem, id=item_id, cart=cart)
        item.delete()
        messages.success(request, 'Item removed from cart.')
    return redirect('cart_summary')

# Update quantity of an item in the cart
def cart_update(request):
    if request.method == 'POST':
        item_id = request.POST.get('item_id')
        quantity = int(request.POST.get('quantity', 1))

        cart = get_or_create_cart(request)
        item = get_object_or_404(CartItem, id=item_id, cart=cart)
        item.quantity = quantity
        item.save()
        messages.success(request, 'Cart updated.')
    return redirect('cart_summary')
