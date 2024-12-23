from rest_framework import serializers
from .models import BoostSales, UpperBanner, LowerBanner


class BoostSalesSerializer(serializers.ModelSerializer):
    month_display = serializers.CharField(source='get_month_display', read_only=True)

    class Meta:
        model = BoostSales
        fields = ['id', 'month', 'month_display', 'sales_qnt', 'is_active_updating_the_photo_menu']


class UpperBannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = UpperBanner
        fields = ['id', 'title', 'description', 'image']


class LowerBannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = LowerBanner
        fields = ['id', 'title', 'description', 'image']
