from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import AboutUs
from .serializers import AboutUsSerializer


class AboutUsAPIView(APIView):
    def get(self, request):
        about_us = AboutUs.objects.all()
        serializer = AboutUsSerializer(about_us, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
