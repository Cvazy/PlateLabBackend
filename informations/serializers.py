from rest_framework import serializers
from .models import HowItsWork, FAQ


class HowItsWorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = HowItsWork
        fields = ['id', 'title', 'description']


class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = ['id', 'question', 'answer']
