from eq.models import Character, Event, Item, Klass, Race, Server
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


class PatchedItemSerializer(serializers.Serializer):
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
        # see https://www.django-rest-framework.org/api-guide/serializers/#writable-nested-representations
        # TODO: figure out how django handles transactions here
        raid = self._create_raid(validated_data)
        self._create_attendees(validated_data, raid)
        self._create_items(validated_data, raid)
        return 
    
    def _create_raid(self, validated_data) -> Raid:
        event = Event.objects.create(name=validated_data['name'])
        raid = Raid.objects.create(date=validated_data['date'], attendance_value=validated_data['attendance'], event=event)
        return raid

    def _create_attendees(self, validated_data: dict, raid: Raid) -> list[Raider]:
        
        # TODO: check with Alex:  should this method fail if the character already exist?
        temp_eqclass = Klass.objects.create(name='foo', short_name='bar')
        temp_eqrace = Race.objects.create(name='hobbits', short_name='hob')
        temp_server = Server.objects.create(name='server', short_name='ser')

        # bulk_create seems to misbehave
        # see caveats: https://docs.djangoproject.com/en/4.1/ref/models/querysets/#bulk-create
        characters = []
        for raider in validated_data['raiders']:
            c = Character.objects.create(
                name=raider, 
                eqclass=temp_eqclass, 
                eqrace=temp_eqrace, 
                server=temp_server
            )
            characters.append(c)

        raiders = Raider.objects.bulk_create(
            [
                Raider(character=character, raid=raid)
                for character in characters
            ], ignore_conflicts=True
        )

        return raiders

    def _create_items(self, validated_data: dict, raid: Raid):
        # TODO: what is the difference between an `Item` and `Loot` here?  should this also create `Loot`?
        return Item.objects.bulk_create([
            Item(
                name=item['name'],
                event=raid.event,
                dkp=item['points']
            )
            for item in validated_data['loots']
        ], ignore_conflicts=True)

