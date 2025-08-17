from django.apps import AppConfig


class GrowatConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'growat'


    def ready(self):
        import growat.translation