from django.apps import AppConfig


class DeyeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'deye'


    def ready(self):
        import deye.translation