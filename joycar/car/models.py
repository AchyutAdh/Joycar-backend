from django.db import models
from django.contrib.auth.models import User

class Car(models.Model):
    name = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.PositiveIntegerField()
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='car/', blank=True, null=True)
    status = models.CharField(max_length=50, choices=[('active', 'Active'), ('inactive', 'Inactive'), ('cancelled', 'Cancelled'), ('completed', 'Completed')])
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cars')

    def __str__(self):
        return self.name


class Auction(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='auctions')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    end_time = models.DateTimeField()
    winner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='won_auctions')


class Bid(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.auction} - {self.price}"