from django.apps import AppConfig


class CheckoutConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'checkout'

 # Override the ready method to perform actions when the application is ready
    def ready(self):
         # Import signals module from the checkout app
        import checkout.signals