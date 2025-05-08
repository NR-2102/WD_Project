from django.apps import AppConfig

class StoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'  # Specifies the default auto-incrementing field type for primary keys
    name = 'store'  # The name of the app
