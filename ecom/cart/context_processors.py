from .models import Cart  # Import the Cart model from the current app's models

# Context processor function to make cart data available in all templates
def cart(request):
    """Make cart data available in all templates"""
    try:
        # If the user is logged in, try to get the Cart associated with the user
        if request.user.is_authenticated:
            cart = Cart.objects.get(user=request.user)
        else:
            # If the user is not logged in, try to get cart ID from session
            cart_id = request.session.get('cart_id')
            if cart_id:
                # Try to get the cart by ID from the database
                cart = Cart.objects.get(id=cart_id)
            else:
                # No cart ID in session, cart is None
                cart = None
    except Cart.DoesNotExist:
        # If no cart is found in the database, set cart to None
        cart = None
    
    # If cart doesn't exist, return default empty values
    if cart is None:
        return {
            'cart': None,
            'cart_items_count': 0,
            'cart_total': 0
        }
    
    # If cart exists, return it along with total items and total price
    return {
        'cart': cart,
        'cart_items_count': cart.get_total_items(),  # Method to get number of items in the cart
        'cart_total': cart.get_total_price()         # Method to get total price of items in the cart
    } 
