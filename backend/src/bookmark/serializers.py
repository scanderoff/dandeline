from typing import Any
from rest_framework import serializers

from src.catalog.serializers import ProductSerializer
from .services.bookmark import Bookmark


class BookmarkItemSerializer(serializers.Serializer):
    product = ProductSerializer()


class BookmarkSerializer(serializers.Serializer):
    total_items = serializers.SerializerMethodField()
    items = serializers.SerializerMethodField()

    def get_total_items(self, instance: Bookmark) -> int:
        return len(instance)

    def get_items(self, instance: Bookmark) -> dict[str, Any]:
        return BookmarkItemSerializer(instance, many=True).data
