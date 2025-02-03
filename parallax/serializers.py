from rest_framework import serializers
from .models import Parallax, Image


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['id', 'image', 'caption']


class ParallaxSerializer(serializers.ModelSerializer):
    gallery = ImageSerializer(many=True, read_only=True)

    class Meta:
        model = Parallax
        fields = ['id', 'up_title', 'down_title', 'image',  'gallery']
