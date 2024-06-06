from django.apps import AppConfig


class MindcraftwebConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mindcraftweb'

    def ready(self):
        import mindcraftweb.signals
