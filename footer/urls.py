from django.urls import path
from .views import FooterAPIView, NetworkAPIView

urlpatterns = [
    path('api/v1/footer', FooterAPIView.as_view(), name='footer'),
    path('api/v1/networks', NetworkAPIView.as_view(), name='networks'),
]
