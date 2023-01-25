from .models import Raid, Loot, Raider
from rest_framework import serializers


class RaidSerializer(serializers.ModelSerializer):
    class Meta:
        model = Raid
        fields = "__all__"


class LootSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loot
        fields = "__all__"


class RaiderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Raider
        fields = "__all__"

class ImportSerializer(serializers.ListSerializer):
    def create(self, validated_data):
        return super().create(validated_data)