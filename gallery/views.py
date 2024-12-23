from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Gallery
from .serializers import GallerySerializer


class GalleryAPIView(APIView):
    def get(self, request):
        galleries = Gallery.objects.all()
        serializer = GallerySerializer(galleries, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
