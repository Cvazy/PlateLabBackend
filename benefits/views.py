from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import BoostSales, UpperBanner, LowerBanner
from .serializers import BoostSalesSerializer, UpperBannerSerializer, LowerBannerSerializer


class BoostSalesAPIView(APIView):
    def get(self, request):
        boost_sales = BoostSales.objects.all()
        serializer = BoostSalesSerializer(boost_sales, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UpperBannerAPIView(APIView):
    def get(self, request):
        upper_banners = UpperBanner.objects.all()
        serializer = UpperBannerSerializer(upper_banners, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class LowerBannerAPIView(APIView):
    def get(self, request):
        lower_banners = LowerBanner.objects.all()
        serializer = LowerBannerSerializer(lower_banners, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
