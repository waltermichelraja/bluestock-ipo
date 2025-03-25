from django.urls import path
from .views import update_user_profile, get_watchlist, add_to_watchlist, remove_from_watchlist

urlpatterns = [
    path('profile', update_user_profile, name='update_user_profile'),
    path('watchlist', get_watchlist, name='get_watchlist'),
    path('watchlist/add', add_to_watchlist, name='add_to_watchlist'),
    path('watchlist/<int:stockId>/remove', remove_from_watchlist, name='remove_from_watchlist'),
]
