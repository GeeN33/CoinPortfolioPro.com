from django.core.management.base import BaseCommand, CommandError
from portfolio_app.services import CalculatePortfolio


class Command(BaseCommand):
    help = 'calculate_portfolio'

    def handle(self, *args, **options):
        CalculatePortfolio()