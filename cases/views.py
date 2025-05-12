from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Case, Image
from .serializers import CaseSerializer, ImageSerializer


class CaseAPIView(APIView):
    def get(self, request):
        cases = Case.objects.all()
        serializer = CaseSerializer(cases, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
    def post(self, request):
        case_data = {
            'restaurant_name': request.data.get('restaurant_name'),
            'description': request.data.get('description', '')
        }
        
        case_serializer = CaseSerializer(data=case_data)
        if case_serializer.is_valid():
            case = case_serializer.save()
            
            images = request.data.getlist('images')
            if images:
                for image in images:
                    image_data = {
                        'album': case.id,
                        'image': image,
                        'caption': ''
                    }
                    image_serializer = ImageSerializer(data=image_data)
                    if image_serializer.is_valid():
                        image_serializer.save()
                    else:
                        return Response(image_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
            return Response(CaseSerializer(case).data, status=status.HTTP_201_CREATED)
        return Response(case_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
