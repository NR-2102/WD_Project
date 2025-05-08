from django.urls import path
from . import views  # Import views from the current app

# Define URL patterns for the cart functionality
urlpatterns = [
    # URL for viewing the cart summary page
    path('', views.cart_summary, name='cart_summary'),
    
    # URL to add a product to the cart (expects data via POST)
    path('add/', views.cart_add, name='cart_add'),
    
    # URL to delete an item from the cart (expects data via POST)
    path('delete/', views.cart_delete, name='cart_delete'),
    
    # URL to update the quantity of an item in the cart (expects data via POST)
    path('update/', views.cart_update, name='cart_update'),
]
