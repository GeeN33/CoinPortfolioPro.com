import requests
from django.conf import settings
COINMARKETCAP_KEY = settings.COINMARKETCAP_KEY

COINSTATS_KEY = settings.COINSTATS_KEY

COMPARE_KEY = settings.COMPARE_KEY

def get_historical_data(symbol, time_start, time_end, count):
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/ohlcv/historical'

    parameters = {
        'symbol': symbol,
        'time_start': time_start.strftime('%Y-%m-%d'),
        'time_end': time_end.strftime('%Y-%m-%d'),
        'count': count,
        'interval': 'daily'  # Можно изменить на 'hourly', 'daily', 'weekly', 'monthly' и т.д.
    }

    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': COINMARKETCAP_KEY,
    }

    response = requests.get(url, headers=headers, params=parameters)
    data = response.json()

    return data


def get_historical_coinstats(coin, interval='24h', limit=100):
    # URL для запроса исторических данных

    url = f"https://openapiv1.coinstats.app/coins/{coin}/charts?period={interval}&limit={limit}"

    headers = {
        "accept": "application/json",
        "X-API-KEY": COINSTATS_KEY
    }

    # Отправляем GET запрос
    response = requests.get(url, headers=headers)

    # Проверяем статус ответа
    if response.status_code == 200:
        # Преобразуем ответ из формата JSON
        data = response.json()
        return data
    else:
        print("Ошибка при получении данных:", response.status_code)
        return None

def fetch_crypto_data(fsym, tsym, limit):
    url = f"https://min-api.cryptocompare.com/data/v2/histominute"
    parameters = {
        'fsym': fsym,
        'tsym': tsym,
        'limit': limit,
        'timeframe': 'histoday',
        'api_key': COMPARE_KEY
    }
    response = requests.get(url, params=parameters)
    data = response.json()
    return data

