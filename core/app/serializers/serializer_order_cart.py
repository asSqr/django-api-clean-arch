from rest_framework import serializers
from core.models import OrderCart


class CreateOrderCartSerializer(serializers.Serializer):
    name = serializers.SerializerMethodField()

    def get_name(*args, **kwargs):
        return 'a'
