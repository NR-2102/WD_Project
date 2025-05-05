from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from store.models import Products
from .models import Cart, CartItem

def get_or_create_cart(request):
    """Get existing cart or create a new one"""
    try:
        if request.user.is_authenticated:
            cart, created = Cart.objects.get_or_create(user=request.user)
        else:
            cart_id = request.session.get('cart_id')
            if cart_id:
                try:
                    cart = Cart.objects.get(id=cart_id)
                except Cart.DoesNotExist:
                    cart = Cart.objects.create()
                    request.session['cart_id'] = cart.id
            else:
                cart = Cart.objects.create()
                request.session['cart_id'] = cart.id
        return cart
    except Exception as e:
        messages.error(request, f'Error accessing cart: {str(e)}')
        return None

def cart_summary(request):
    """Display cart contents"""
    cart = get_or_create_cart(request)
    if not cart:
        return redirect('home')
    
    items = cart.items.all()
    context = {
        'cart': cart,
        'items': items,
        'total_price': cart.get_total_price(),
        'total_items': cart.get_total_items()
    }
    return render(request, 'cart_summary.html', context)

def cart_add(request):
    """Add product to cart"""
    if request.method == 'POST':
        try:
            product_id = request.POST.get('product_id')
            quantity = int(request.POST.get('quantity', 1))
            
            if not product_id:
                messages.error(request, 'Product ID is required')
                return redirect('home')
            
            # Get product and cart
            product = get_object_or_404(Products, id=product_id)
            cart = get_or_create_cart(request)
            
            if not cart:
                messages.error(request, 'Could not access cart')
                return redirect('home')
            
            # Add or update cart item
            cart_item, created = CartItem.objects.get_or_create(
                cart=cart,
                product=product,
                defaults={'quantity': quantity}
            )
            
            if not created:
                cart_item.quantity += quantity
                cart_item.save()
            
            messages.success(request, f'{product.name} added to cart')
            return redirect('cart_summary')
            
        except ValueError:
            messages.error(request, 'Invalid quantity')
            return redirect('home')
        except Exception as e:
            messages.error(request, f'Error adding to cart: {str(e)}')
            return redirect('home')
    
    return redirect('home')

def cart_delete(request):
    """Remove item from cart"""
    if request.method == 'POST':
        try:
            item_id = request.POST.get('item_id')
            if not item_id:
                messages.error(request, 'Item ID is required')
                return redirect('cart_summary')
            
            cart = get_or_create_cart(request)
            if not cart:
                messages.error(request, 'Could not access cart')
                return redirect('home')
            
            item = cart.items.get(id=item_id)
            product_name = item.product.name
            item.delete()
            messages.success(request, f'{product_name} removed from cart')
            
        except CartItem.DoesNotExist:
            messages.error(request, 'Item not found in cart')
        except Exception as e:
            messages.error(request, f'Error removing item: {str(e)}')
    
    return redirect('cart_summary')

def cart_update(request):
    """Update item quantity in cart"""
    if request.method == 'POST':
        try:
            item_id = request.POST.get('item_id')
            quantity = int(request.POST.get('quantity', 1))
            
            if not item_id:
                messages.error(request, 'Item ID is required')
                return redirect('cart_summary')
            
            if quantity < 1:
                messages.error(request, 'Quantity must be at least 1')
                return redirect('cart_summary')
            
            cart = get_or_create_cart(request)
            if not cart:
                messages.error(request, 'Could not access cart')
                return redirect('home')
            
            item = cart.items.get(id=item_id)
            item.quantity = quantity
            item.save()
            messages.success(request, 'Cart updated successfully')
            
        except CartItem.DoesNotExist:
            messages.error(request, 'Item not found in cart')
        except ValueError:
            messages.error(request, 'Invalid quantity')
        except Exception as e:
            messages.error(request, f'Error updating cart: {str(e)}')
    
    return redirect('cart_summary')
