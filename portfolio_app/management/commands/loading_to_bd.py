from django.core.management.base import BaseCommand, CommandError

from portfolio_app.models import Exchange, Event, Portfolio, PortfolioItem, Transaction
from portfolio_app.services import Loading_To_bd


class Command(BaseCommand):
    help = 'loading_to_bd'

    def handle(self, *args, **options):
        Loading_To_bd()


