from django.urls import path
from .views import get_all_stocks, get_stock_data, get_stock_history, search_stocks, get_trending_stocks

urlpatterns = [
    path('trending/', get_trending_stocks, name='get_trending_stocks'),
    path('search/<str:query>/', search_stocks, name='search_stocks'),
    path('<str:symbol>/history/', get_stock_history, name='get_stock_history'),
    path('<str:symbol>/', get_stock_data, name="get_stock_data"),
    path('', get_all_stocks, name="get_all_stocks"),
]
