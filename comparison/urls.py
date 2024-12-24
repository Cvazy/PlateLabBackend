from django.urls import path
from .views import ComparisonAPIView

urlpatterns = [
    path('api/v1/comparisons', ComparisonAPIView.as_view(), name='comparisons'),
]
