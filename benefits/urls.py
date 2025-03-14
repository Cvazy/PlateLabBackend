from django.urls import path
from .views import BoostSalesAPIView

urlpatterns = [
    path('api/v1/boost-sales', BoostSalesAPIView.as_view(), name='boost-sales'),
]
