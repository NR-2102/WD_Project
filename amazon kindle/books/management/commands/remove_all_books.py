from django.core.management.base import BaseCommand
from books.models import Book
from django.db import transaction

class Command(BaseCommand):
    help = 'Removes all books from the database'

    def add_arguments(self, parser):
        parser.add_argument(
            '--force',
            action='store_true',
            help='Force removal without confirmation',
        )

    def handle(self, *args, **options):
        if not options['force']:
            confirm = input('Are you sure you want to remove all books? This action cannot be undone. [y/N]: ')
            if confirm.lower() != 'y':
                self.stdout.write(self.style.WARNING('Operation cancelled.'))
                return

        try:
            with transaction.atomic():
                count = Book.objects.count()
                Book.objects.all().delete()
                self.stdout.write(self.style.SUCCESS(f'Successfully removed {count} books from the database.'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error removing books: {str(e)}')) 