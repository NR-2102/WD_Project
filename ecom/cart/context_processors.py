# Import the Cart model from the current app's models
from .models import Cart

# Context processor function to make cart data available in all templates
def cart(request):
    """Make cart data available in all templates"""
    try:
        # If the user is logged in, get the cart associated with the user
        if request.user.is_authenticated:
            cart = Cart.objects.get(user=request.user)
        else:
            # If the user is not authenticated, try to get cart using session
            cart_id = request.session.get('cart_id')
            if cart_id:
                cart = Cart.objects.get(id=cart_id)
            else:
                cart = None
    except Cart.DoesNotExist:
        # If no cart is found in the database, set cart to None
        cart = None

    # If no cart exists, return default values
    if cart is None:
        return {
            'cart': None,
            'cart_items_count': 0,
            'cart_total': 0
        }

    # If cart exists, return cart object along with total items and total price
    return {
        'cart': cart,
        'cart_items_count': cart.get_total_items(),
        'cart_total': cart.get_total_price()
    }
