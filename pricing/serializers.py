from rest_framework import serializers
from .models import Pricing


class PricingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pricing
        fields = ['id', 'min_photo_qnt', 'max_photo_qnt', 'price', 'is_the_best_price']
