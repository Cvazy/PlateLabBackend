from django.urls import path
from .views import CaseAPIView

urlpatterns = [
    path('api/v1/cases', CaseAPIView.as_view(), name='cases'),
]
