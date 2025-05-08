"""
===========================================
 URL Configuration for Kindle Clone Project
===========================================

This file maps URLs to views. It defines which views are called for 
specific URL paths. We also include necessary settings to serve 
media files during development.

For more details on URL configuration, visit:
https://docs.djangoproject.com/en/5.2/topics/http/urls/

===========================================
"""

# ========== Importing Necessary Modules ==========
# Importing the Django admin site for the admin interface.
from django.contrib import admin
# Importing path and include to define URL routes.
from django.urls import path, include
# Importing settings to access project settings.
from django.conf import settings
# Importing static function to serve media files in development.
from django.conf.urls.static import static

# Importing views for login and logout functionality from the books app.
from books.views import logout_view, login_view

# ========== URL Patterns ==========
# The urlpatterns list is used to route URLs to appropriate views.
# Each path corresponds to a specific URL pattern and the associated view.

urlpatterns = [
    # Path for the Django admin interface.
    path('admin/', admin.site.urls),
    
    # Include the URLs from the 'books' app (which handles book-related functionality).
    path('', include('books.urls')),

    # Path for user login functionality, routed to the login_view function.
    path('login/', login_view, name='login'),

    # Path for user logout functionality, routed to the logout_view function.
    path('logout/', logout_view, name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# This ensures that media files (like images, uploaded by users) are served correctly
# when running the Django development server. 
# In production, this should be handled by a web server (e.g., Nginx or Apache).
