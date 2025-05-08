from django.core.management.base import BaseCommand
from books.models import Book
import requests
import os
from django.conf import settings
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
import time

class Command(BaseCommand):
    help = 'Downloads cover images for books from a placeholder service'

    def handle(self, *args, **kwargs):
        books = Book.objects.all()
        self.stdout.write(f'Found {books.count()} books to process')
        
        # Create media directory if it doesn't exist
        media_root = settings.MEDIA_ROOT
        book_covers_dir = os.path.join(media_root, 'book_covers')
        os.makedirs(book_covers_dir, exist_ok=True)
        
        for book in books:
            if book.cover_image:
                self.stdout.write(f'Book "{book.title}" already has a cover image')
                continue
                
            self.stdout.write(f'Downloading cover for "{book.title}"...')
            
            # Use a placeholder image service with the book title
            # This is just for demonstration - in a real app, you'd use actual book cover images
            try:
                # Use a placeholder service that generates images with text
                # Format: https://via.placeholder.com/300x400?text=Book+Title
                title_for_url = book.title.replace(' ', '+')
                url = f'https://via.placeholder.com/300x400?text={title_for_url}'
                
                response = requests.get(url)
                if response.status_code == 200:
                    # Create a filename based on the book title
                    filename = f'book_covers/{book.id}_{title_for_url}.jpg'
                    
                    # Save the image
                    book.cover_image.save(filename, ContentFile(response.content), save=True)
                    self.stdout.write(self.style.SUCCESS(f'Successfully downloaded cover for "{book.title}"'))
                    
                    # Add a small delay to avoid overwhelming the server
                    time.sleep(0.5)
                else:
                    self.stdout.write(self.style.ERROR(f'Failed to download cover for "{book.title}": HTTP {response.status_code}'))
            except Exception as e:
                self.stdout.write(self.style.ERROR(f'Error downloading cover for "{book.title}": {str(e)}'))
        
        self.stdout.write(self.style.SUCCESS('Cover download process completed')) 