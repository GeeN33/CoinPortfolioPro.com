import time

from portfolio_app.models import Portfolio, PortfolioItem, Event, Transaction, Exchange
import requests

from tg_bot.bot import bot
from tg_bot.models import ProfileTg
from django.conf import settings

YOUR_API_KEY = settings.COINMARKETCAP_KEY
# URL запроса к API CoinMarketCap
url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'

def get_price_last(coin_name):

    # Параметры запроса
    parameters = {
        'symbol': coin_name,  # Укажите символ интересующей вас криптовалюты
        'convert': 'USD'  # Укажите валюту, в которую вы хотите конвертировать цену
    }

    # Заголовок с вашим ключом API
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': YOUR_API_KEY,
    }

    # Отправка запроса
    response = requests.get(url, headers=headers, params=parameters)

    # Обработка ответа
    data = response.json()

    # Извлечение цены из ответа
    if 'status' in data and data['status']['error_code'] == 0:
        price = data['data'][coin_name]['quote']['USD']['price']
        print(f"Последняя цена {coin_name}: ${price}")
        return float(price)
    else:
        print("Ошибка при получении данных")
        return 0

def CalculatePortfolio():
    portfolio = Portfolio.objects.filter(user_id=1).first()

    items = PortfolioItem.objects.filter(portfolio=portfolio)
    balance = 0
    profit_sum1 = 0
    amount_sum1 = 0
    for item in items:
         transactions = item.transactions.filter(calculate=True)
         for transaction in transactions:
           time.sleep(2)
           price_last = get_price_last(item.coin_name)
           if price_last > 0:
               profit = (price_last * transaction.amount) - (transaction.price_open * transaction.amount)
               amount_sum = transaction.price_open * transaction.amount
               percent = (profit / (amount_sum / 100))
               transaction.price_last = price_last
               transaction.percent = percent
               transaction.profit = profit
               transaction.save()


         transactions = item.transactions.filter(calculate=True)
         profit_sum = 0
         amount_sum = 0
         for transaction in transactions:
             balance = balance + (transaction.price_last * transaction.amount)
             profit_sum = profit_sum + transaction.profit
             amount_sum = amount_sum + (transaction.price_open * transaction.amount)

         item.profit = profit_sum
         item.percent =  (profit_sum / (amount_sum / 100))
         item.save()
         profit_sum1 = profit_sum1 + profit_sum
         amount_sum1 =  amount_sum1 + amount_sum

    portfolio.balance = balance
    portfolio.profit = profit_sum1
    portfolio.percent =  (profit_sum1 / ( amount_sum1 / 100))
    portfolio.save()

def Top10():
    tg = ProfileTg.objects.filter()
    if tg:
        for t in tg:
            items = PortfolioItem.objects.filter(portfolio=t.portfolio).order_by('-percent')[:10]
            text='Top 10:'
            for item in items:
                text = text + f'\n {item.coin_name} - {item.percent:.2f}%'
            print(text)
            bot.send_message(t.chatid, text)

def EventPortfolio():
    events = Event.objects.all()
    for event in events:
        portfolioites = event.portfolioitem_set.all()
        for portfolioite in portfolioites:
            if portfolioite.notified == False and portfolioite.percent > event.target:
                  portfolioite.event.remove(event)
                  tg = ProfileTg.objects.filter(portfolio=portfolioite.portfolio)
                  if tg:
                      for t in tg:
                          bot.send_message(t.chatid, f'Цель достигнута {portfolioite.coin_name} {portfolioite.percent:.2f}%')
                  print(portfolioite.coin_name, portfolioite.percent)

def EventUpdata():
    PortfolioItem.objects.all().update(notified=False)


def Loading_To_bd():
    print('start')
    exchanges = ['bybit.com', 'okx.com']
    coins = [
        {
            'name': 'JUP',
            'exchange': 1,
            'price_open': 0.5889,
            'amount': 178.87,
        },
        {
            'name': 'PORT3',
            'exchange': 1,
            'price_open': 0.08004,
            'amount': 831.24,
        },
        {
            'name': 'STG',
            'exchange': 1,
            'price_open': 0.6681,
            'amount': 147.77,
        },
        {
            'name': 'RACA',
            'exchange': 1,
            'price_open': 0.00016182,
            'amount': 275366.2181,
        },
        {
            'name': 'STRK',
            'exchange': 1,
            'price_open': 1.914,
            'amount': 49.7,
        },
        {
            'name': 'BCUT',
            'exchange': 1,
            'price_open': 0.30045,
            'amount': 320,
        },
        {
            'name': 'MBOX',
            'exchange': 1,
            'price_open': 0.3393,
            'amount': 209.46,
        },
        {
            'name': 'GMX',
            'exchange': 1,
            'price_open': 53.7493,
            'amount': 1.71828,
        },
        {
            'name': 'CAKE',
            'exchange': 1,
            'price_open': 4.0886,
            'amount': 17.803,
        },
        {
            'name': 'HFT',
            'exchange': 1,
            'price_open': 0.4463,
            'amount': 142.53,
        },
        {
            'name': 'GMT',
            'exchange': 1,
            'price_open': 0.2646,
            'amount': 206.48,
        },
        {
            'name': 'SHRAP',
            'exchange': 1,
            'price_open': 0.30208,
            'amount': 205.1946,
        },
        {
            'name': 'TOMI',
            'exchange': 1,
            'price_open': 1.013,
            'amount': 69.83,
        },
        {
            'name': 'FIL',
            'exchange': 1,
            'price_open': 7.946,
            'amount': 6.14385,
        },
        {
            'name': 'MINA',
            'exchange': 1,
            'price_open': 1.6756,
            'amount': 41.28867,
        },
        {
            'name': 'VIC',
            'exchange': 1,
            'price_open': 0.77,
            'amount': 42.677,
        },
        {
            'name': 'MEME',
            'exchange': 1,
            'price_open': 0.04272,
            'amount': 1055.69,
        },
        {
            'name': 'XAI',
            'exchange': 1,
            'price_open': 1.24327,
            'amount': 29.07,
        },
        {
            'name': 'MANTA',
            'exchange': 1,
            'price_open': 2.7712,
            'amount': 11.06,
        },
        {
            'name': 'APE',
            'exchange': 1,
            'price_open': 2.1336,
            'amount': 16.64,
        },
        {
            'name': 'SC',
            'exchange': 1,
            'price_open': 0.009604,
            'amount': 3127.10976,
        },
        {
            'name': 'XCH',
            'exchange': 2,
            'price_open': 32.62,
            'amount': 4.26,
        },
        {
            'name': 'CVX',
            'exchange': 2,
            'price_open': 5.358,
            'amount': 20.0226,
        },
        {
            'name': 'APM',
            'exchange': 2,
            'price_open': 0.00605,
            'amount': 9493.77,
        },
        {
            'name': 'SNX',
            'exchange': 2,
            'price_open': 4.516,
            'amount': 13.224,
        },
        {
            'name': 'GOAL',
            'exchange': 2,
            'price_open': 0.051,
            'amount': 998.525,
        },
    ]

    Exchange.objects.get_or_create(name=exchanges[0])
    Exchange.objects.get_or_create(name=exchanges[1])
    event7 = Event.objects.get_or_create(target=700)[0]
    event10 = Event.objects.get_or_create(target=1000)[0]
    event15 = Event.objects.get_or_create(target=1500)[0]
    portfolio = Portfolio.objects.get_or_create(user_id=1, name='Best')[0]

    for coin in coins:
        portfolioitem = \
        PortfolioItem.objects.get_or_create(portfolio=portfolio, exchange_id=coin['exchange'], coin_name=coin['name'])[
            0]
        Transaction.objects.get_or_create(coin=portfolioitem, price_open=coin['price_open'], amount=coin['amount'])
        portfolioitem.event.add(event7)
        portfolioitem.event.add(event10)
        portfolioitem.event.add(event15)
        portfolioitem.save()


