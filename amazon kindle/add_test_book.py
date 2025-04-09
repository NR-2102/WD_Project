import os
import django

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'kindle_clone.settings')
django.setup()

from books.models import Book

# Create a test book if it doesn't exist
if not Book.objects.filter(title="The Great Gatsby").exists():
    Book.objects.create(
        title="The Great Gatsby",
        author="F. Scott Fitzgerald",
        description="The Great Gatsby is a 1925 novel by American writer F. Scott Fitzgerald. Set in the Jazz Age on Long Island, near New York City, the novel depicts first-person narrator Nick Carraway's interactions with mysterious millionaire Jay Gatsby and Gatsby's obsession to reunite with his former lover, Daisy Buchanan.",
        price=9.99
    )
    print("Test book 'The Great Gatsby' created successfully!")
else:
    print("Test book already exists.") 