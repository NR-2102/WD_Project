from django.apps import AppConfig

# Configuration for the 'store' app
class StoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'  # Default field type for primary keys
    name = 'store'  # The name of the app, used in Django settings
