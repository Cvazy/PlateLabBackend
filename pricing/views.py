from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Pricing
from .serializers import PricingSerializer


class PricingAPIView(APIView):
    def get(self, request):
        pricing = Pricing.objects.all()
        serializer = PricingSerializer(pricing, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
