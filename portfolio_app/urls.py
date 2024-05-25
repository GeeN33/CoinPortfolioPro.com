from django.urls import path

from portfolio_app.views import PortfolioView

urlpatterns = [

path('portfolios', PortfolioView.as_view(), name='portfolios'),

]


