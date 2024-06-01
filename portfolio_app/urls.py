from django.urls import path

from portfolio_app.views import PortfolioView, PortfolioDetailView

urlpatterns = [

path('portfolios', PortfolioView.as_view(), name='portfolios'),

path('portfolio', PortfolioDetailView.as_view(), name='portfolios'),

]


