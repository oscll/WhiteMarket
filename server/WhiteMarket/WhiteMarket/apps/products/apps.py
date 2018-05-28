from django.apps import AppConfig


class ProductsConfig(AppConfig):
    name = 'WhiteMarket.apps.products'

    def ready(self):
        import WhiteMarket.apps.products.signals
