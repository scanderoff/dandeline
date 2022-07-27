from rest_framework import serializers

from .models import HeroSlide, Contact


class HeroSlideSerializer(serializers.ModelSerializer):
    class Meta():
        model = HeroSlide
        fields = "__all__"


class ContactSerializer(serializers.ModelSerializer):
    class Meta():
        model = Contact
        fields = "__all__"
