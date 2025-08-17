from django.apps import AppConfig


class SkidkaProductConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'skidka_product'

    def ready(self):
        import skidka_product.translation