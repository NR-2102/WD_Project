from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    # path('checkout/', views.checkout, name='checkout'),
    path('product/<int:pk>/', views.product_description, name='product'),
    path('category/<str:category_name>/', views.category_name, name='category'),
    path('cart/', views.cart, name='cart'),
    path('deals/', views.deals, name='deals'),
    
    
]