"""
===============================================
 WSGI Configuration for Kindle Clone Project
===============================================

This file configures the WSGI (Web Server Gateway Interface) for the project. 
It exposes the WSGI callable as a module-level variable named ``application``, 
which is used by web servers to communicate with the Django application.

For more information, refer to the Django documentation:
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/

===============================================
"""

# ========== Importing Required Modules ==========
# Importing the os module to set the environment variable for Django settings.
import os

# Importing the get_wsgi_application function from Django to get the WSGI application.
from django.core.wsgi import get_wsgi_application

# ========== Setting the Environment Variable ==========
# Set the default settings module for the Django application.
# This tells Django where to find the settings file.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'kindle_clone.settings')

# ========== WSGI Application ==========
# Get the WSGI application that can be used by a web server to communicate with Django.
# The `application` object will be exposed to the web server.
application = get_wsgi_application()
