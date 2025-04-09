from django.contrib import admin
from .models import Book, UserLibrary

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'price', 'created_at')
    search_fields = ('title', 'author')
    list_filter = ('created_at',)

@admin.register(UserLibrary)
class UserLibraryAdmin(admin.ModelAdmin):
    list_display = ('user',)
    filter_horizontal = ('books',)
