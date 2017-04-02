from django.apps import AppConfig
from .generator import *
class PortfolioConfig(AppConfig):
    name = 'portfolio'
    verbose_name = "CryptoWealth"
    def ready(self):
        print('Initializing...')
        rebalance_all(False)