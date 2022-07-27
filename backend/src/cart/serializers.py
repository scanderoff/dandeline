from typing import Any

from rest_framework import serializers

from src.catalog.serializers import VariationSerializer
from .services.cart import Cart


class CartItemSerializer(serializers.Serializer):
    variation = VariationSerializer()
    quantity = serializers.IntegerField()
    total_price = serializers.DecimalField(max_digits=10, decimal_places=2)


class CartSerializer(serializers.Serializer):
    total_items = serializers.SerializerMethodField()
    total_price = serializers.DecimalField(max_digits=10, decimal_places=2)
    items = serializers.SerializerMethodField()

    def get_total_items(self, instance: Cart) -> int:
        return len(instance)

    def get_items(self, instance: Cart) -> dict[str, Any]:
        return CartItemSerializer(instance, many=True).data

