from django.urls import path
from .views import get_portfolio, add_stock_to_portfolio, update_stock_in_portfolio, remove_stock_from_portfolio, get_portfolio_performance

urlpatterns = [
    path('performance/', get_portfolio_performance, name='get_portfolio_performance'),
    path('add/', add_stock_to_portfolio, name='add_stock_to_portfolio'),
    path('<int:stock_id>/update/', update_stock_in_portfolio, name='update_stock_in_portfolio'),
    path('<int:stock_id>/delete/', remove_stock_from_portfolio, name='remove_stock_from_portfolio'),
    path('', get_portfolio, name='get_portfolio'),
]
