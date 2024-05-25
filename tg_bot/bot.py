import telebot
from telebot import types

from django.conf import settings

from portfolio_app.models import Portfolio, PortfolioItem
from tg_bot.models import ProfileTg

token = settings.TG_TOKEN
bot = telebot.TeleBot(token)
@bot.message_handler(commands=['start'])
def start_message(message):
    text="""Привет!\nДля активации бота введите код активации."""
    bot.send_message(message.chat.id, text)
@bot.message_handler(commands=['help'])
def start_message(message):
    text="""/start\n/balance\n/top10"""
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['balance'])
def start_message(message):
    pp = Portfolio.objects.filter(tgbots__chatid=message.chat.id).first()
    bot.send_message(message.chat.id, str(pp))

@bot.message_handler(commands=['top10'])
def start_message(message):
    tg = ProfileTg.objects.filter()
    if tg:
        for t in tg:
            items = PortfolioItem.objects.filter(portfolio=t.portfolio).order_by('-percent')[:10]
            text = 'Top 10:'
            for item in items:
                text = text + f'\n {item.coin_name} - {item.percent:.2f}%'
            bot.send_message(t.chatid, text)

@bot.message_handler(content_types=['text'])
def message_reply(message):
    if message.text != "":
        print(message.text)
        pp = ProfileTg.objects.filter(active_code=message.text).last()
        if pp:
            pp.chatid = message.chat.id
            pp.name=message.from_user.first_name
            pp.active=True
            pp.save()
            bot.send_message(message.chat.id,'Ты активирован')
        else:
            bot.send_message(message.chat.id, 'Код не верный')


