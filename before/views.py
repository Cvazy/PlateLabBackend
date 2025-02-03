from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import RestaurantSerializer, ParametersSerializer


class ParametersAPIView(APIView):
    def get(self, request):
        parameters = Parameters.objects.all()
        serializer = ParametersSerializer(parameters, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class RestaurantAPIView(APIView):
    def get(self, request):
        restaurant = Restaurant.objects.all()
        serializer = RestaurantSerializer(restaurant, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
