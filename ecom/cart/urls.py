# Import the path function to define URL patterns
from django.urls import path
# Import views from the current app
from . import views

# List of URL patterns for the cart app
urlpatterns = [
    # URL pattern for viewing the cart summary page
    path('', views.cart_summary, name='cart_summary'),

    # URL pattern for adding a product to the cart
    path('add/', views.cart_add, name='cart_add'),

    # URL pattern for deleting a product from the cart
    path('delete/', views.cart_delete, name='cart_delete'),

    # URL pattern for updating a product's quantity in the cart
    path('update/', views.cart_update, name='cart_update'),
]
