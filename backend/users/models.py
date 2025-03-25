from django.db import models
from django.contrib.auth.models import User

class Watchlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stock_symbol = models.CharField(max_length=10)
    company_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.user.username} - {self.stock_symbol}"
