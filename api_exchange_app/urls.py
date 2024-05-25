from django.urls import path

from api_exchange_app.views import CoinMarketCapHistoryView, CoinstatsHistoryView, CryptocompareHistoryView

urlpatterns = [

path('coin-marketcap-history', CoinMarketCapHistoryView.as_view(), name='coin-marketcap-history'),

path('coinstats-history', CoinstatsHistoryView.as_view(), name='coinstats-history'),

path('cryptocompare-history', CryptocompareHistoryView.as_view(), name='cryptocompare-history'),

]
