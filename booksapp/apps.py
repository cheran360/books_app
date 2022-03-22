from django.apps import AppConfig


class BooksappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'booksapp'

    def ready(self):
        import booksapp.signals
