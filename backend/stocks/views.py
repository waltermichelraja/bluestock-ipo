import requests
from django.conf import settings
from django.core.cache import cache
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes

BASE_URL = "https://www.alphavantage.co/query"

@api_view(['GET'])
@permission_classes([AllowAny])
def get_stock_data(request, symbol):
    cache_key = f"stock_details_{symbol}"
    cached_data = cache.get(cache_key)

    if cached_data:
        return Response(cached_data)

    params = {
        "function": "OVERVIEW",
        "symbol": symbol,
        "apikey": settings.ALPHA_VANTAGE_API_KEY
    }

    response = requests.get(BASE_URL, params=params)

    if response.status_code == 200:
        data = response.json()
        stock_info = {
            "symbol": data.get("Symbol"),
            "name": data.get("Name"),
            "description": data.get("Description"),
            "sector": data.get("Sector"),
            "industry": data.get("Industry"),
            "currency": data.get("Currency"),
            "country": data.get("Country"),
            "market_cap": data.get("MarketCapitalization"),
            "ebitda": data.get("EBITDA"),
            "pe_ratio": data.get("PERatio"),
            "dividend_yield": data.get("DividendYield"),
            "market_open": "09:30",
            "market_close": "16:00",
            "timezone": "UTC-05"
        }

        cache.set(cache_key, stock_info, timeout=86400)
        return Response(stock_info)

    return Response({"error": "Failed to fetch stock details"}, status=500)

@api_view(['GET'])
@permission_classes([AllowAny])
def search_stocks(request, query):
    params = {
        "function": "SYMBOL_SEARCH",
        "keywords": query,
        "apikey": settings.ALPHA_VANTAGE_API_KEY
    }

    response = requests.get(BASE_URL, params=params)

    if response.status_code == 200:
        data = response.json().get("bestMatches", [])
        stocks = [
            {"symbol": stock["1. symbol"], "name": stock["2. name"]}
            for stock in data
        ]
        return Response({"stocks": stocks})

    return Response({"error": "Failed to fetch stock symbols"}, status=500)

@api_view(['GET'])
@permission_classes([AllowAny])
def get_stock_history(request, symbol):
    cache_key = f"stock_history_{symbol}"
    cached_data = cache.get(cache_key)

    if cached_data:
        return Response(cached_data)

    params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": symbol,
        "apikey": settings.ALPHA_VANTAGE_API_KEY
    }

    response = requests.get(BASE_URL, params=params)

    if response.status_code != 200:
        return Response({"error": "Failed to fetch stock history"}, status=500)

    data = response.json()

    if "Time Series (Daily)" not in data:
        return Response({"error": "No historical data available for this stock"}, status=404)

    historical_data = []
    for date, values in data["Time Series (Daily)"].items():
        historical_data.append({
            "date": date,
            "open": values.get("1. open", "N/A"),
            "high": values.get("2. high", "N/A"),
            "low": values.get("3. low", "N/A"),
            "close": values.get("4. close", "N/A"),
            "volume": values.get("5. volume", "N/A")
        })

    historical_data.sort(key=lambda x: x["date"], reverse=True)

    cache.set(cache_key, historical_data, timeout=86400)

    return Response(historical_data)