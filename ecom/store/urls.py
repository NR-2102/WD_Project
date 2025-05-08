from django.urls import path
from . import views  # Importing the views from the current app

urlpatterns = [
    # Home page route
    path('', views.home, name='home'),
    
    # Search results page, triggered when a user performs a search
    path('search/', views.search_results, name='search_results'),
    
    # Login route, where users can log in
    path('login/', views.login_user, name='login'),
    
    # Logout route, to log out a user
    path('logout/', views.logout_user, name='logout'),
    
    # Register route for users to sign up
    path('register/', views.register_user, name='register'),
    
    # Product detail page, dynamically loading product information based on product ID
    path('product/<int:pk>/', views.product_description, name='product'),
    
    # Category page, displaying products in a specific category
    path('category/<str:category_name>/', views.category_name, name='category'),
    
    # Profile page, showing user-specific information and settings
    path('profile/', views.profile, name='profile'),
    
    # Checkout page for finalizing orders
    path('checkout/', views.checkout, name='checkout'),
    
    # Change password route for users to update their password
    path('change-password/', views.change_password, name='change_password'),
    
    # Order confirmation page, displaying confirmation details based on the order number
    path('order-confirmation/<str:order_number>/', views.order_confirmation, name='order_confirmation'),
    
    # Order history route, showing a user’s past orders
    path('order-history/', views.order_history, name='order_history'),
]
