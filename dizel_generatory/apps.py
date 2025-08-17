from django.apps import AppConfig


class DizelGeneratoryConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'dizel_generatory'


    def ready(self):
        import dizel_generatory.translation