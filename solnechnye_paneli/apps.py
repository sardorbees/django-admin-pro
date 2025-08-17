from django.apps import AppConfig


class SolnechnyePaneliConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'solnechnye_paneli'


    def ready(self):
        import solnechnye_paneli.translation