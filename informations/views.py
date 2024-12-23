from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import HowItsWork, FAQ
from .serializers import HowItsWorkSerializer, FAQSerializer


class HowItsWorkAPIView(APIView):
    def get(self, request):
        how_its_work = HowItsWork.objects.all()
        serializer = HowItsWorkSerializer(how_its_work, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class FAQAPIView(APIView):
    def get(self, request):
        faqs = FAQ.objects.all()
        serializer = FAQSerializer(faqs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
