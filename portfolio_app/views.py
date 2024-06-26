from rest_framework.response import Response
from rest_framework.views import APIView

from portfolio_app.models import Portfolio, PortfolioItem
from portfolio_app.serializers import PortfolioSerializer
from django.db.models import Prefetch

class PortfolioView(APIView):
    def get(self, request):

        queryset = Portfolio.objects.filter(public=True).prefetch_related(
            Prefetch('portfolioitem_set', queryset=PortfolioItem.objects.prefetch_related('transactions'))
        )
        serializer_for_queryset = PortfolioSerializer(
            queryset,
            many=True
        )
        return Response(serializer_for_queryset.data)

class PortfolioDetailView(APIView):
    def get(self, request):
        queryset = Portfolio.objects.filter(public=True).prefetch_related(
            Prefetch('portfolioitem_set', queryset=PortfolioItem.objects.prefetch_related('transactions'))
        ).last()
        print(queryset)
        return Response([])



