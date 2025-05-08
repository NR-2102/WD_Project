from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page of the website, routed to the 'home' view
    path('search/', views.search_results, name='search_results'),  # Search results page, routed to the 'search_results' view
    path('login/', views.login_user, name='login'),  # User login page, routed to the 'login_user' view
    path('logout/', views.logout_user, name='logout'),  # User logout, routed to the 'logout_user' view
    path('register/', views.register_user, name='register'),  # User registration page, routed to the 'register_user' view
    path('product/<int:pk>/', views.product_description, name='product'),  # Product details page, using primary key (pk) for a specific product
    path('category/<str:category_name>/', views.category_name, name='category'),  # Category page, using category name for filtering
    path('profile/', views.profile, name='profile'),  # User profile page, routed to the 'profile' view
    path('checkout/', views.checkout, name='checkout'),  # Checkout page for users, routed to the 'checkout' view
    path('change-password/', views.change_password, name='change_password'),  # Change password page, routed to the 'change_password' view
    path('order-confirmation/<str:order_number>/', views.order_confirmation, name='order_confirmation'),  # Order confirmation page, using order number to display the order status
    path('order-history/', views.order_history, name='order_history'),  # User's order history page, routed to the 'order_history' view
]
