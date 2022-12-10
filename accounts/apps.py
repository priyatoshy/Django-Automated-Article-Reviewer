from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'
    
    
    #letting django know about the signals.py method
    def ready(self):
        import accounts.signals