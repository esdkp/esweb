from eq.serializers import ItemSerializer
from .models import Raid, Loot, Raider
from rest_framework import serializers
from drf_writable_nested.serializers import WritableNestedModelSerializer

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


class PatchedItemSerializer(serializers.Serializer):
    """

    """

    name = serializers.CharField()
    raider = serializers.CharField()
    points = serializers.FloatField()

class ImportSerializer(serializers.Serializer):
    # also look into https://github.com/beda-software/drf-writable-nested
    """
    meta-serializer for several other 'real' serializers

    for more see https://www.django-rest-framework.org/api-guide/serializers/#dealing-with-nested-objects
    """
    date = serializers.DateTimeField()
    name = serializers.CharField()
    attendance = serializers.IntegerField(default=0)
    raiders = serializers.ListField(child=serializers.CharField(), allow_empty=False)
    loots = PatchedItemSerializer(many=True)

    def create(self, validated_data):
        return super().create(validated_data)