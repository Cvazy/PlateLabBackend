from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Parallax
from .serializers import ParallaxSerializer


class ParallaxAPIView(APIView):
    def get(self, request):
        parallax = Parallax.objects.all()
        serializer = ParallaxSerializer(parallax, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
