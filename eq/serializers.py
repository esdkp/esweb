from .models import Character, Expansion, Guild, Klass, Race, Server
from rest_framework import serializers


class CharacterSerializer(serializers.HyperlinkedModelSerializer):
    eqclass = serializers.StringRelatedField(read_only=True)
    eqrace = serializers.StringRelatedField(read_only=True)
    guild = serializers.HyperlinkedRelatedField(view_name="guild-detail", read_only=True)
    server = serializers.HyperlinkedRelatedField(view_name="server-detail", read_only=True)

    class Meta:
        model = Character
        # fields = "__all__"
        fields = ["name", "surname", "eqclass", "eqrace", "guild", "server"]


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
