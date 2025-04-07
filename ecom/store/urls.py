from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_user, name='login'),
    path('register/', views.register_user, name='register'),
    path('logout/', views.logout_user, name='logout'),
    # path('cart/', views.cart, name='cart'),
    # path('checkout/', views.checkout, name='checkout'),
    path('product/<int:pk>/', views.product, name='product'),
    path('category/<str:foo>/', views.category, name='category'),
    path('deals/', views.deals, name='deals'),
    path('description/', views.description, name='description'),
    path('product/<int:pk>/description/', views.description, name='product_description'),
]