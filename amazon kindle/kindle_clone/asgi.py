"""
============================================================
 ASGI CONFIGURATION FILE FOR DJANGO PROJECT 'kindle_clone'
============================================================

This file sets up the ASGI (Asynchronous Server Gateway Interface)
application for your Django project, which is used for handling 
asynchronous web protocols like WebSockets, HTTP/2, etc.

It exposes the ASGI application callable as a module-level variable 
named `application`.

For more info, see:
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
"""

# ========== Import Required Modules ==========
import os
from django.core.asgi import get_asgi_application

# ========== Set the Default Django Settings Module ==========
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'kindle_clone.settings')

# ========== Get the ASGI Application ==========
application = get_asgi_application()
