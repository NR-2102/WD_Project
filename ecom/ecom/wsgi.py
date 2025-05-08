"""
WSGI config for ecom project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

# Import necessary modules
import os
from django.core.wsgi import get_wsgi_application

# Set the default Django settings module for the 'ecom' project
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecom.settings')

# Get the WSGI application callable to be used by WSGI servers
application = get_wsgi_application()
