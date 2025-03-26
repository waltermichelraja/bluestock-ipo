import requests
from django.conf import settings
from django.core.cache import cache
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

BASE_URL = "https://financialmodelingprep.com/api/v3"
API_KEY = settings.FMP_API_KEY

@api_view(['GET'])
@permission_classes([AllowAny])
def get_all_stocks(request):
    cache_key = "all_stocks"
    cached_data = cache.get(cache_key)
    
    if cached_data:
        return Response(cached_data)
    
    url = f"{BASE_URL}/stock/list?apikey={API_KEY}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        cache.set(cache_key, data, timeout=86400)
        return Response(data)
    
    return Response({"error": "Failed to fetch stock list"}, status=500)

@api_view(['GET'])
@permission_classes([AllowAny])
def get_stock_data(request, symbol):
    cache_key = f"stock_details_{symbol}"
    cached_data = cache.get(cache_key)
    
    if cached_data:
        return Response(cached_data)
    
    url = f"{BASE_URL}/profile/{symbol}?apikey={API_KEY}"
    response = requests.get(url)
    
    if response.status_code == 200 and response.json():
        data = response.json()[0]
        stock_info = {
            "symbol": data.get("symbol"),
            "name": data.get("companyName"),
            "industry": data.get("industry"),
            "sector": data.get("sector"),
            "market_cap": data.get("mktCap"),
            "currency": data.get("currency"),
            "price": data.get("price"),
            "exchange": data.get("exchange"),
            "ceo": data.get("ceo"),
            "website": data.get("website")
        }
        cache.set(cache_key, stock_info, timeout=86400)
        return Response(stock_info)
    
    return Response({"error": "Failed to fetch stock details"}, status=500)

@api_view(['GET'])
@permission_classes([AllowAny])
def search_stocks(request, query):
    url = f"{BASE_URL}/search?query={query}&limit=10&apikey={API_KEY}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        stocks = [
            {
                "symbol": stock.get("symbol"),
                "name": stock.get("name"),
                "currency": stock.get("currency"),
                "stockExchange": stock.get("stockExchange")
            }
            for stock in data
        ]
        return Response({"stocks": stocks})
    
    return Response({"error": "Failed to fetch stock symbols"}, status=500)

@api_view(['GET'])
@permission_classes([AllowAny])
def get_stock_history(request, symbol):
    url = f"{BASE_URL}/historical-price-full/{symbol}?apikey={API_KEY}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        historical_data = [
            {
                "date": entry.get("date"),
                "open": entry.get("open"),
                "high": entry.get("high"),
                "low": entry.get("low"),
                "close": entry.get("close"),
                "volume": entry.get("volume")
            }
            for entry in data.get("historical", [])
        ]
        return Response({"symbol": symbol, "historical": historical_data})
    
    return Response({"error": "Failed to fetch historical data"}, status=500)

@api_view(['GET'])
@permission_classes([AllowAny])
def get_trending_stocks(request):
    url = f"{BASE_URL}/stock_market/gainers?apikey={API_KEY}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        trending_stocks = [
            {
                "symbol": stock.get("symbol"),
                "name": stock.get("name"),
                "price": stock.get("price"),
                "change": stock.get("change"),
                "change_percent": stock.get("changesPercentage")
            }
            for stock in data
        ]
        return Response({"trending_stocks": trending_stocks})

    return Response({"error": "Failed to fetch trending stocks"}, status=500)

