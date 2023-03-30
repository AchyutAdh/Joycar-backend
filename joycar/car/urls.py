from django.urls import path
from .views import AuctionDetailAPIView, BidListAPIView, BidListAllAPIView, CarCreateAPIView, CarListAPIView, AuctionCreateAPIView, BidCreateAPIView, ActiveAuctionListAPIView

urlpatterns = [
    path('cars/', CarListAPIView.as_view(), name='car_list'),
    path('cars/create/', CarCreateAPIView.as_view(), name='car_create'),
    path('auctions/create/', AuctionCreateAPIView.as_view(), name='auction_create'),
    path('auctions/<int:pk>/bid/', BidCreateAPIView.as_view(), name='bid_create'),
    path('auctions/active/', ActiveAuctionListAPIView.as_view(), name='active_auction_list'),
    path('auctions/<int:pk>/', AuctionDetailAPIView.as_view(), name='auction_detail'),
    path('auctions/<int:pk>/bids/', BidListAPIView.as_view(), name='bid-list'),
    path('bids/', BidListAllAPIView.as_view(), name='bid-list-all'),
]