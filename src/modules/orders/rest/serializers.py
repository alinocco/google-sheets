from rest_framework import serializers
from ..models import Order

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = [
            'uuid',
            'number',
            'order',
            'price_in_dollars',
            'price_in_rubles',
            'delivery_date',
        ]