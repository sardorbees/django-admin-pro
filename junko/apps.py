from django.apps import AppConfig


class JunkoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'junko'

    def ready(self):
        import junko.translation