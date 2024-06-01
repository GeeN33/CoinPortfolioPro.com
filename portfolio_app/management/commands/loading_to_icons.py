from django.core.management.base import BaseCommand, CommandError

from portfolio_app.coins_icons.path_coin_list import loading_To_icons


class Command(BaseCommand):
    help = 'loading_to_icons'

    def handle(self, *args, **options):
        loading_To_icons()