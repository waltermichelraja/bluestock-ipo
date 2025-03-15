from django.conf import settings
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from decimal import Decimal
from .models import Portfolio, PortfolioStock, PortfolioPerformance
from .serializers import PortfolioSerializer, PortfolioStockSerializer, PortfolioPerformanceSerializer
import requests

API_KEY = settings.FMP_API_KEY
FMP_API_URL = "https://financialmodelingprep.com/api/v3/quote"

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_portfolio(request):
    user = request.user

    portfolio, created = Portfolio.objects.get_or_create(user=user)
    serializer = PortfolioSerializer(portfolio)
    
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_stock_to_portfolio(request):
    user = request.user
    data = request.data

    symbol = data.get("symbol")
    quantity = data.get("quantity")
    purchase_price = data.get("purchase_price")

    if not symbol or not quantity or not purchase_price:
        return Response({"error": "symbol, quantity, and purchase_price are required"}, status=status.HTTP_400_BAD_REQUEST)

    portfolio, _ = Portfolio.objects.get_or_create(user=user)
    stock, created = PortfolioStock.objects.get_or_create(portfolio=portfolio, stock_symbol=symbol)

    if created:
        stock.quantity = quantity
        stock.purchase_price = purchase_price
    else:
        stock.quantity += quantity
        stock.purchase_price = ((stock.purchase_price * stock.quantity) + (purchase_price * quantity)) / (stock.quantity + quantity)

    stock.save()

    return Response(PortfolioStockSerializer(stock).data, status=status.HTTP_201_CREATED)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def remove_stock_from_portfolio(request, stock_id):
    user = request.user

    try:
        stock = PortfolioStock.objects.get(id=stock_id, portfolio__user=user)
        stock.delete()
        return Response({"message": "Stock removed successfully"}, status=status.HTTP_204_NO_CONTENT)
    except PortfolioStock.DoesNotExist:
        return Response({"error": "Stock not found in portfolio"}, status=status.HTTP_404_NOT_FOUND)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_stock_in_portfolio(request, stock_id):
    user = request.user
    data = request.data

    try:
        stock = PortfolioStock.objects.get(id=stock_id, portfolio__user=user)

        stock.quantity = data.get("quantity", stock.quantity)
        stock.purchase_price = data.get("purchase_price", stock.purchase_price)
        stock.save()

        return Response(PortfolioStockSerializer(stock).data, status=status.HTTP_200_OK)
    except PortfolioStock.DoesNotExist:
        return Response({"error": "Stock not found in portfolio"}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_portfolio_performance(request):
    user = request.user

    try:
        portfolio = Portfolio.objects.get(user=user)
        stocks = PortfolioStock.objects.filter(portfolio=portfolio)

        total_investment = 0
        total_current_value = 0

        for stock in stocks:
            response = requests.get(f"{FMP_API_URL}/{stock.stock_symbol}?apikey={API_KEY}")
            if response.status_code == 200:
                data = response.json()
                if data:
                    current_price = data[0].get("price", stock.purchase_price)
                    total_investment += stock.quantity * stock.purchase_price
                    total_current_value += stock.quantity * current_price

        gain_loss = float(total_current_value) - float(total_investment)
        percentage_change = (gain_loss / float(total_investment)) * 100 if total_investment else 0

        performance, created = PortfolioPerformance.objects.get_or_create(portfolio=portfolio, defaults={
            "total_value": 0.0,
            "gain_loss": 0.0,
            "percentage_change": 0.0
        })

        performance.total_value = float(total_current_value) if stocks.exists() else 0.0
        performance.gain_loss = float(gain_loss) if stocks.exists() else 0.0
        performance.percentage_change = float(percentage_change) if stocks.exists() else 0.0

        performance.save()

        serializer = PortfolioPerformanceSerializer(performance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    except Portfolio.DoesNotExist:
        return Response({"error": "Portfolio not found"}, status=status.HTTP_404_NOT_FOUND)
