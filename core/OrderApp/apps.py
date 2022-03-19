from django.apps import AppConfig


class OrderappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'OrderApp'

    def ready(self):
        import OrderApp.api.signals