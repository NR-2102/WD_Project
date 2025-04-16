from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('library/', views.my_library, name='my_library'),
    path('add-to-library/<int:book_id>/', views.add_to_library, name='add_to_library'),
    path('remove-from-library/<int:book_id>/', views.remove_from_library, name='remove_from_library'),
    path('bulk-remove-from-library/', views.bulk_remove_from_library, name='bulk_remove_from_library'),
    path('profile/', views.profile, name='profile'),
    path('book/<int:book_id>/', views.book_detail, name='book_detail'),
] 