import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecom.settings')
django.setup()

from store.models import Category

def create_categories():
    categories = [
        'Clothes',
        'Health & Personal Care',
        'Furniture',
        'Mobile and Accessories',
        'Makeup Kit',
        'Pet Food & More',
        'Toys & More',
        'Fashion & More'
    ]
    
    for category_name in categories:
        category, created = Category.objects.get_or_create(name=category_name)
        if created:
            print(f"Created category: {category_name}")
        else:
            print(f"Category already exists: {category_name}")

if __name__ == '__main__':
    create_categories() 