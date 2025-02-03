from django.urls import path
from .views import *

urlpatterns = [
    path('api/v1/before/restaurant', RestaurantAPIView.as_view(), name='restaurant'),
    path('api/v1/before/parameters', ParametersAPIView.as_view(), name='parameters'),
]
