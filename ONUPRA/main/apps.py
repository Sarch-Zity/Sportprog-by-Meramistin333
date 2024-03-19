from django.apps import AppConfig


class MainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main'
    verbose_name = 'Main'
    label = 'main'
    
    def ready(self):
        # Implicitly connect signal handlers decorated with @receiver.
        from . import signals