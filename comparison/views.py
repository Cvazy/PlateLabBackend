from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Comparison
from .serializers import ComparisonSerializer


class ComparisonAPIView(APIView):
    def get(self, request):
        comparisons = Comparison.objects.all()
        serializer = ComparisonSerializer(comparisons, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
