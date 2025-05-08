from django.core.management.base import BaseCommand
from books.models import Book
from django.conf import settings
import os
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
from django.core.files.base import ContentFile

class Command(BaseCommand):
    help = 'Generates placeholder cover images for books without covers'

    def handle(self, *args, **options):
        # Create media directory if it doesn't exist
        media_root = settings.MEDIA_ROOT
        covers_dir = os.path.join(media_root, 'book_covers')
        os.makedirs(covers_dir, exist_ok=True)

        # Get all books without cover images
        books = Book.objects.filter(cover_image='')
        self.stdout.write(f'Found {books.count()} books without cover images')

        try:
            # Try to load a font, fall back to default if not available
            try:
                font = ImageFont.truetype("arial.ttf", 40)
                small_font = ImageFont.truetype("arial.ttf", 20)
            except:
                font = ImageFont.load_default()
                small_font = ImageFont.load_default()

            for book in books:
                self.stdout.write(f'Generating cover for "{book.title}"...')
                
                # Create a new image with a gradient background
                img = Image.new('RGB', (300, 400), color='white')
                draw = ImageDraw.Draw(img)
                
                # Draw gradient background
                for y in range(400):
                    r = int(200 + (y / 400) * 55)  # Gradient from light to darker blue
                    g = int(220 + (y / 400) * 35)
                    b = int(240 + (y / 400) * 15)
                    draw.line([(0, y), (300, y)], fill=(r, g, b))

                # Add title (wrapped if too long)
                title = book.title
                words = title.split()
                lines = []
                current_line = []
                
                for word in words:
                    current_line.append(word)
                    line = ' '.join(current_line)
                    if draw.textlength(line, font=font) > 280:  # Leave some margin
                        if len(current_line) > 1:
                            current_line.pop()
                            lines.append(' '.join(current_line))
                            current_line = [word]
                        else:
                            lines.append(line)
                            current_line = []
                
                if current_line:
                    lines.append(' '.join(current_line))

                # Draw title
                y_position = 100
                for line in lines:
                    text_width = draw.textlength(line, font=font)
                    x_position = (300 - text_width) / 2
                    draw.text((x_position, y_position), line, font=font, fill='black')
                    y_position += 50

                # Add author
                if book.author:
                    author_text = f"By {book.author}"
                    text_width = draw.textlength(author_text, font=small_font)
                    x_position = (300 - text_width) / 2
                    draw.text((x_position, y_position + 20), author_text, font=small_font, fill='darkblue')

                # Add category and price at the bottom
                y_position = 350
                if book.category:
                    category_text = f"Category: {book.category}"
                    text_width = draw.textlength(category_text, font=small_font)
                    x_position = (300 - text_width) / 2
                    draw.text((x_position, y_position), category_text, font=small_font, fill='darkblue')
                    y_position += 25

                price_text = f"${book.price:.2f}"
                text_width = draw.textlength(price_text, font=small_font)
                x_position = (300 - text_width) / 2
                draw.text((x_position, y_position), price_text, font=small_font, fill='darkgreen')

                # Save the image
                img_io = BytesIO()
                img.save(img_io, format='JPEG', quality=85)
                img_io.seek(0)

                # Generate filename
                filename = f'book_{book.id}_cover.jpg'
                
                # Save to the book's cover_image field
                book.cover_image.save(filename, ContentFile(img_io.getvalue()), save=True)
                self.stdout.write(self.style.SUCCESS(f'Successfully generated cover for "{book.title}"'))

        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error generating covers: {str(e)}'))
            return

        self.stdout.write(self.style.SUCCESS('Successfully generated all cover images')) 