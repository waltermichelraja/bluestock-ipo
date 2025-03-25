from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from .models import Watchlist
from .serializers import UserSerializer, WatchlistSerializer

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_user_profile(request):
    user = request.user
    data = request.data

    user.first_name = data.get('first_name', user.first_name)
    user.last_name = data.get('last_name', user.last_name)
    user.email = data.get('email', user.email)

    user.save()
    serializer = UserSerializer(user)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_watchlist(request):
    user = request.user
    watchlist = Watchlist.objects.filter(user=user)
    serializer = WatchlistSerializer(watchlist, many=True)
    return Response({"watchlist": serializer.data}, status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_to_watchlist(request):
    user = request.user
    data = request.data

    stock_symbol = data.get('symbol')
    company_name = data.get('company_name', '')

    if not stock_symbol:
        return Response({"error": "Stock symbol is required"}, status=status.HTTP_400_BAD_REQUEST)

    watchlist_item, created = Watchlist.objects.get_or_create(
        user=user,
        stock_symbol=stock_symbol,
        defaults={"company_name": company_name}
    )

    serializer = WatchlistSerializer(watchlist_item)
    return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def remove_from_watchlist(request, stockId):
    user = request.user
    try:
        watchlist_item = Watchlist.objects.get(id=stockId, user=user)
        watchlist_item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except Watchlist.DoesNotExist:
        return Response({"error": "Stock not found in watchlist"}, status=status.HTTP_404_NOT_FOUND)
