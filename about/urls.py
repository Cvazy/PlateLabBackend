from django.urls import path
from .views import AboutUsAPIView

urlpatterns = [
    path('api/v1/about', AboutUsAPIView.as_view(), name='about-us'),
]
