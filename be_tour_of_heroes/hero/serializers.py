from rest_framework import serializers

from hero.models import Hero


class HeroListCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Hero
        fields = ("id", "firstname")


class HeroRetrieveUpdateSerializer(serializers.ModelSerializer):
    firstname = serializers.CharField(required=False, default="")

    class Meta:
        model = Hero
        fields = ("id", "firstname")
