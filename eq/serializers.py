from .models import Character, Expansion, Guild, Klass, Race, Server, Event, Item
from rest_framework import serializers


class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = "__all__"


class ExpansionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expansion
        fields = "__all__"


class GuildSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guild
        fields = "__all__"


class KlassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Klass
        fields = "__all__"


class RaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Race
        fields = "__all__"


class ServerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Server
        fields = "__all__"


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = "__all__"


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = "__all__"
