from django.urls import path
from .views import PricingAPIView

urlpatterns = [
    path('api/v1/pricing', PricingAPIView.as_view(), name='pricing'),
]
