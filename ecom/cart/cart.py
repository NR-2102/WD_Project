# Define a Cart class to handle shopping cart functionality
class Cart():
    # Constructor method; takes the HTTP request object as a parameter
    def __init__(self, request):
        
        # Store the session object from the request
        self.session = request.session
        
        # Try to get the cart data from the session using a key
        cart = self.session.get('session_key')
        
        # If 'session_key' doesn't exist in the session, create an empty cart dictionary
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}

        # Assign the cart (whether retrieved or newly created) to the instance variable
        self.cart = cart
