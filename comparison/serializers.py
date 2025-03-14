from rest_framework import serializers
from .models import Comparison


class ComparisonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comparison
        fields = ['id', 'title', 'photo_for_difference', 'price_per_photo', 'convenience_for_restaurants',
                  'style_and_customization']
