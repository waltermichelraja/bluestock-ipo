from rest_framework import serializers
from .models import Portfolio, PortfolioStock, PortfolioPerformance

class PortfolioStockSerializer(serializers.ModelSerializer):
    class Meta:
        model = PortfolioStock
        fields = ['id', 'stock_symbol', 'quantity', 'purchase_price', 'purchase_date']

class PortfolioSerializer(serializers.ModelSerializer):
    stocks = PortfolioStockSerializer(many=True, read_only=True)
    
    class Meta:
        model = Portfolio
        fields = ['id', 'user', 'created_at', 'stocks']
        read_only_fields = ['user', 'created_at']

class PortfolioPerformanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = PortfolioPerformance
        fields = ['id', 'portfolio', 'total_value', 'gain_loss', 'percentage_change', 'last_updated']
