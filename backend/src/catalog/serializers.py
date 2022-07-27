from rest_framework import serializers

from .models import Product, Variation


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class VariationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Variation
        fields = ("id",)
