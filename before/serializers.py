from rest_framework import serializers
from .models import *


class SwiperElementSerializer(serializers.ModelSerializer):
    class Meta:
        model = SwiperElement
        fields = [
            'id',
            'item_name',
            'image',
            'caption',
            'price',
            'min_cal_value',
            'max_cal_value'
        ]


class ItemFromProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemFromProductList
        fields = [
            'id',
            'item_name',
            'image',
            'caption',
            'price',
            'min_cal_value',
            'max_cal_value',
            'description'
        ]


class RestaurantSerializer(serializers.ModelSerializer):
    swiper_items = SwiperElementSerializer(many=True, read_only=True)
    product_list_items = ItemFromProductListSerializer(many=True, read_only=True)

    class Meta:
        model = Restaurant
        fields = [
            'id',
            'name',
            'swiper_title',
            'items_list_title',
            'swiper_items',
            'product_list_items'
        ]


class ParametersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parameters
        fields = ['id', 'name', 'start_value', 'end_value']


class PartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partner
        fields = ['id', 'name', 'image']
