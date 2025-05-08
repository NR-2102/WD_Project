"""
URL configuration for ecom project.

The `urlpatterns` list routes URLs to views.
For more info, see: https://docs.djangoproject.com/en/5.1/topics/http/urls/
"""

from django.contrib import admin
from django.urls import path, include
from . import settings
from django.conf.urls.static import static

urlpatterns = [
    # Admin panel URL
    path('admin/', admin.site.urls),

    # Main store URLs (handles homepage and product-related views)
    path('', include('store.urls')),

    # Cart-related URLs (add, delete, update, summary)
    path('cart/', include('cart.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # Serves media files during development
