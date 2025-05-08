# Define the Cart class to manage shopping cart operations
class Cart():
    def __init__(self, request):
        # Store the session object from the request
        self.session = request.session

        # Try to retrieve the cart dictionary from the session using the key 'session_key'
        cart = self.session.get('session_key')

        # If 'session_key' is not present in the session, initialize it as an empty dictionary
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}

        # Assign the cart dictionary to the instance variable for further use
        self.cart = cart
