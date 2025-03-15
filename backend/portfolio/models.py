from django.db import models
from django.contrib.auth.models import User

class Portfolio(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class PortfolioStock(models.Model):
    stock_symbol = models.CharField(max_length=10)
    quantity = models.PositiveIntegerField(null=True, blank=True)
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    purchase_date = models.DateField(auto_now_add=True)
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE, related_name='stocks')

 
class PortfolioPerformance(models.Model):
    portfolio = models.OneToOneField(Portfolio, on_delete=models.CASCADE, related_name='performance')
    total_value = models.DecimalField(max_digits=15, decimal_places=2)
    gain_loss = models.DecimalField(max_digits=15, decimal_places=2)
    percentage_change = models.DecimalField(max_digits=5, decimal_places=2)
    last_updated = models.DateTimeField(auto_now=True)
