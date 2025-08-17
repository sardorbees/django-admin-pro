from django.apps import AppConfig


class InvertoryConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'invertory'

    def ready(self):
        import invertory.translation