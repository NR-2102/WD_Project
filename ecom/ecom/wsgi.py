"""
WSGI config for ecom project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more info, see:
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application  # Import the WSGI application function

# Set the default settings module for the 'wsgi' application
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecom.settings')

# Create the WSGI application callable
application = get_wsgi_application()
