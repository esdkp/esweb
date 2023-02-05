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


class PatchedItemSerializer(ItemSerializer):
    """
    handles rename logic for base `ItemSerializer
    """

    # TODO: this isn't actually overwriting the `name` property from `ItemSerializer`
    name = serializers.CharField(source='Name')

class ImportSerializer(serializers.Serializer):
    # also look into https://github.com/beda-software/drf-writable-nested
    """
    meta-serializer for several other 'real' serializers

    for more see https://www.django-rest-framework.org/api-guide/serializers/#dealing-with-nested-objects
    """

    loots = PatchedItemSerializer(many=True)