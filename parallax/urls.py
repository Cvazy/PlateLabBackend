from django.urls import path
from .views import ParallaxAPIView

urlpatterns = [
    path('api/v1/parallax', ParallaxAPIView.as_view(), name='parallax'),
]
