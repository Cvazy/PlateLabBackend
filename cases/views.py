from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Case
from .serializers import CaseSerializer


class CaseAPIView(APIView):
    def get(self, request):
        cases = Case.objects.all()
        serializer = CaseSerializer(cases, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
