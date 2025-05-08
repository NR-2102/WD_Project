#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

def main():
    """Run administrative tasks."""
    
    # Set the default Django settings module. This tells Django which settings to use.
    # In this case, it points to the 'settings.py' file inside the 'ecom' directory.
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecom.settings')
    
    try:
        # Import and execute Django's management commands (such as 'runserver', 'migrate', etc.)
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        # If Django cannot be imported, raise an ImportError with a helpful message
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    
    # Execute the command passed as a command-line argument (e.g., python manage.py runserver)
    execute_from_command_line(sys.argv)

# Entry point for when the script is run directly
if __name__ == '__main__':
    main()
