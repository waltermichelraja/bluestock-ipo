from django.urls import path
from .views import get_stock_data, get_stock_history, search_stocks

urlpatterns = [
    path('<str:symbol>/', get_stock_data, name="get_stock_data"),
    path('<str:symbol>/history/', get_stock_history, name='get_stock_history'),
    path('search/<str:query>/', search_stocks, name='search_stocks'),
    
]
