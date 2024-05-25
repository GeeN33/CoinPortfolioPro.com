from django.core.management.base import BaseCommand, CommandError
from portfolio_app.services import EventPortfolio
from tg_bot.bot import bot


class Command(BaseCommand):
    help = 'bot_run'

    def handle(self, *args, **options):
        print('bot_run')
        bot.infinity_polling()