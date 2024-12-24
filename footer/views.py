from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Footer, Network
from .serializers import FooterSerializer, NetworkSerializer


class FooterAPIView(APIView):
    def get(self, request):
        footers = Footer.objects.all()
        serializer = FooterSerializer(footers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class NetworkAPIView(APIView):
    def get(self, request):
        networks = Network.objects.all()
        serializer = NetworkSerializer(networks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
