from django.urls import path
from .views import HowItsWorkAPIView, FAQAPIView

urlpatterns = [
    path('api/v1/how-it-works', HowItsWorkAPIView.as_view(), name='how-it-works'),
    path('api/v1/faqs', FAQAPIView.as_view(), name='faqs'),
]
