from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import BoostSales
from .serializers import BoostSalesSerializer


class BoostSalesAPIView(APIView):
    def get(self, request):
        boost_sales = BoostSales.objects.all()
        serializer = BoostSalesSerializer(boost_sales, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
