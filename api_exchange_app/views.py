from django.http import JsonResponse
from rest_framework.views import APIView
from datetime import datetime, timedelta
import json
from api_exchange_app.services import get_historical_data, get_historical_coinstats, fetch_crypto_data

class CoinMarketCapHistoryView(APIView):
    def get(self, request):
        time_end = datetime.now()
        time_start = time_end - timedelta(days=100)
        historical_data = get_historical_data('BTC', time_start, time_end, 100)

        print(historical_data)

        return JsonResponse(historical_data, safe=False, json_dumps_params={"ensure_ascii": True}, status=200)

class CoinstatsHistoryView(APIView):
    def get(self, request):
        coin = 'bitcoin'

        historical_data = get_historical_coinstats(coin)

        if historical_data:
            historical_data = historical_data
        else:
            historical_data=[]

        return JsonResponse(historical_data, safe=False, json_dumps_params={"ensure_ascii": True}, status=200)

class CryptocompareHistoryView(APIView):
    def get(self, request):
        # cryptocompare-history?symbol=XRP&limit=120
        symbol = self.request.GET.get('symbol', 'BTC')
        limit = self.request.GET.get('limit', '100')
        FSYM = symbol
        TSYM = 'USD'

        try:
            limit = int(limit)
        except ValueError:
            limit = 100

        crypto_data = fetch_crypto_data(FSYM, TSYM, limit)

        try:

            crypto_data = crypto_data['Data']['Data']

        except KeyError:

            crypto_data = []


        return JsonResponse(crypto_data, safe=False, json_dumps_params={"ensure_ascii": True}, status=200)

