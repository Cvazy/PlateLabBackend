from django.urls import path
from .views import *

urlpatterns = [
    path('api/v1/banners', BannerAPIView.as_view(), name='banners'),
    path('api/v1/partners', PartnerAPIView.as_view(), name='partners'),
]
