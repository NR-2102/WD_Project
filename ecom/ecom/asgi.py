"""
ASGI config for ecom project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

# Import necessary modules
import os
from django.core.asgi import get_asgi_application

# Set the default Django settings module for the 'ecom' project
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecom.settings')

# Get the ASGI application callable to be used by ASGI servers
application = get_asgi_application()
