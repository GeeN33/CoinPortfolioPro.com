from django.contrib.auth.models import User
from django.db import models

class Event(models.Model):
    CHOICES = (
        ('1', 'Percent'),
        ('2', 'Price'),)
    type = models.CharField(max_length=1, choices=CHOICES, default='1')
    target = models.FloatField(default=1000)
    def __str__(self):
        if self.type == '1':
            return f'Percent {self.target}%'
        if self.type == '2':
            return f'Price {self.target}$'
        return self.type
class Exchange(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
class Portfolio(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=100)
    public = models.BooleanField(default=True)
    balance = models.FloatField(null=True, blank=True)
    profit = models.FloatField(null=True, blank=True)
    percent = models.FloatField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)


    def __str__(self):
        if self.balance is None or self.profit is None or self.percent is None:
            return f'Portfolio: {self.name}\n'
        else:
            return f'Portfolio: {self.name}\nbalance: {self.balance:.2f}\nprofit: {self.profit:.2f}\npercent: {self.percent:.2f}'
class PortfolioItem(models.Model):
    CHOICES = (
        ('1', 'Pending'),
        ('2', 'Opened'),
        ('3', 'Closed'),)
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    status = models.CharField(max_length=1, choices=CHOICES, default='2')
    exchange = models.ForeignKey(Exchange, on_delete=models.SET_NULL, null=True)
    coin_name = models.CharField(max_length=100)
    event = models.ManyToManyField(Event, blank=True)
    profit = models.FloatField(null=True, blank=True)
    percent = models.FloatField(null=True, blank=True)
    notified = models.BooleanField(default=False)

    def __str__(self):
        return self.coin_name

    class Meta:
        ordering = ('id',)
        verbose_name = 'Coin'
        verbose_name_plural = 'Coins'
class Transaction(models.Model):
    CHOICES = (
        ('1', 'Pending'),
        ('2', 'Opened'),
        ('3', 'Closed'),)
    status = models.CharField(max_length=1, choices=CHOICES, default='2')
    coin = models.ForeignKey(PortfolioItem, on_delete=models.CASCADE, related_name='transactions')
    amount = models.FloatField()
    profit = models.FloatField(default=0)
    percent = models.FloatField(default=0)
    price_open = models.FloatField(null=True, blank=True)
    price_close = models.FloatField(null=True, blank=True)
    price_last = models.FloatField(null=True, blank=True)
    calculate = models.BooleanField(help_text='учитывать при расчете портфеля', default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)




