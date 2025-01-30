from django.apps import AppConfig

class FeeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'src.services.fee'

    def ready(self):
        import src.services.fee.signals  # Use the full path to import signals
