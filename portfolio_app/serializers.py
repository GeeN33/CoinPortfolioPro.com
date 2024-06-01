from rest_framework import serializers
from .models import Portfolio, PortfolioItem, Transaction, Coin


class CoinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coin
        fields = ['id', 'name', 'icon', 'price_last']


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['id', 'status', 'amount', 'profit', 'percent', 'price_open', 'price_close', 'price_last', 'calculate', 'created_date', 'updated_date']

class PortfolioItemSerializer(serializers.ModelSerializer):
    transactions = TransactionSerializer(many=True, read_only=True)
    coin = CoinSerializer(read_only=True)
    class Meta:
        model = PortfolioItem
        fields = ['id', 'status', 'exchange', 'coin', 'profit', 'percent', 'notified', 'transactions']

class PortfolioSerializer(serializers.ModelSerializer):

    coins = PortfolioItemSerializer(many=True, read_only=True, source='portfolioitem_set')

    class Meta:
        model = Portfolio
        fields = ['id', 'user', 'name', 'public', 'balance', 'profit', 'percent', 'created_date', 'updated_date', 'coins']