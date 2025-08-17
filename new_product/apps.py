from django.apps import AppConfig


class NewProductConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'new_product'


    def ready(self):
        import new_product.translation