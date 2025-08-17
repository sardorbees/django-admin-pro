from django.apps import AppConfig


class GybridConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'gybrid'


    def ready(self):
        import gybrid.translation