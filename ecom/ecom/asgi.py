"""
ASGI config for ecom project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os
from django.core.asgi import get_asgi_application  # Import ASGI application function from Django

# Set the default Django settings module for the 'asgi' application
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecom.settings')

# Create an ASGI application instance that can be used by ASGI servers
application = get_asgi_application()
