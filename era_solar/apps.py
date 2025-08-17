from django.apps import AppConfig


class EraSolarConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'era_solar'


    def ready(self):
        import era_solar.translation