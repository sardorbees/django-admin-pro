from django.apps import AppConfig


class IndividualnyjTeplovojPunktConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'individualnyj_teplovoj_punkt'


    def ready(self):
        import individualnyj_teplovoj_punkt.translation