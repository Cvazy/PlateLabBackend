from django.urls import path
from .views import GalleryAPIView

urlpatterns = [
    path('api/v1/gallery', GalleryAPIView.as_view(), name='gallery'),
]
