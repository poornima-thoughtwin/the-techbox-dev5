from django.apps import AppConfig


class DashboardConfig(AppConfig):
    name = 'dashboard'

    def ready(self): #method just to import the signals
        import dashboard.signals
