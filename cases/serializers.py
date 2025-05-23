from rest_framework import serializers
from .models import Case, Image


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['id', 'image', 'caption', 'album', 'order']
        extra_kwargs = {
            'album': {'write_only': True}
        }


class CaseSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True, read_only=True)

    class Meta:
        model = Case
        fields = ['id', 'restaurant_name', 'description', 'images']
