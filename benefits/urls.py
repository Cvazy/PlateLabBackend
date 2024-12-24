from django.urls import path
from .views import BoostSalesAPIView, UpperBannerAPIView, LowerBannerAPIView

urlpatterns = [
    path('api/v1/boost-sales', BoostSalesAPIView.as_view(), name='boost-sales'),
    path('api/v1/upper-banner', UpperBannerAPIView.as_view(), name='upper-banner'),
    path('api/v1/lower-banner', LowerBannerAPIView.as_view(), name='lower-banner'),
]
