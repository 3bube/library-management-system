from django.apps import AppConfig

# Configuration class for the 'books' app
class BooksConfig(AppConfig):
    # Specify the default primary key field type for models in this app
    default_auto_field = 'django.db.models.BigAutoField'
    
    # Set the name of the app
    name = 'books'
