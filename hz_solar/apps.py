from django.apps import AppConfig


class HzSolarConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'hz_solar'

    def ready(self):
        import hz_solar.translation