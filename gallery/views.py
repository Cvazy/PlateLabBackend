from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Gallery
from .serializers import GallerySerializer


class GalleryAPIView(APIView):
    def get(self, request):
        galleries = Gallery.objects.all()
        serializer = GallerySerializer(galleries, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
    def post(self, request):
        if isinstance(request.data.getlist('image'), list) and len(request.data.getlist('image')) > 1:
            created_objects = []
            description = request.data.get('description', '')
            
            for image in request.data.getlist('image'):
                data = {'description': description, 'image': image}
                serializer = GallerySerializer(data=data)
                if serializer.is_valid():
                    serializer.save()
                    created_objects.append(serializer.data)
                else:
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
            return Response(created_objects, status=status.HTTP_201_CREATED)
        
        serializer = GallerySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
