from django.core.management.base import BaseCommand, CommandError
from portfolio_app.services import EventPortfolio


class Command(BaseCommand):
    help = 'event_portfolio'

    def handle(self, *args, **options):
        EventPortfolio()