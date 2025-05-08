from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('book/<int:book_id>/', views.book_detail, name='book_detail'),
    path('library/', views.library, name='library'),
    path('add-to-library/<int:book_id>/', views.add_to_library, name='add_to_library'),
    path('remove-from-library/<int:book_id>/', views.remove_from_library, name='remove_from_library'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
] 