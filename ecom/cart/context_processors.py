from .models import Cart

def cart(request):
    """Make cart data available in all templates"""
    try:
        if request.user.is_authenticated:
            cart = Cart.objects.get(user=request.user)
        else:
            cart_id = request.session.get('cart_id')
            if cart_id:
                cart = Cart.objects.get(id=cart_id)
            else:
                cart = None
    except Cart.DoesNotExist:
        cart = None
    
    if cart is None:
        return {
            'cart': None,
            'cart_items_count': 0,
            'cart_total': 0
        }
    
    return {
        'cart': cart,
        'cart_items_count': cart.get_total_items(),
        'cart_total': cart.get_total_price()
    } 