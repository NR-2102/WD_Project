# Import the AppConfig class from django.apps
from django.apps import AppConfig

# Define a configuration class for the 'cart' app
class CartConfig(AppConfig):
    # Set the default type of primary key field to BigAutoField
    default_auto_field = 'django.db.models.BigAutoField'
    # Set the name of the app
    name = 'cart'
