from rest_framework import serializers


class ContactSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    email = serializers.EmailField()
    phone = serializers.CharField(max_length=20)
    company = serializers.CharField(max_length=255)
    message = serializers.CharField(required=False, allow_blank=True)
