import datetime

from django.test import TestCase
from eq.factories import CharacterFactory
from eq.models import Item, Event, Character
from .models import Loot, Raid


class RaidTestCase(TestCase):
    def setUp(self):
        Item.objects.create(name="Awesome Loot", dkp=50)
        Item.objects.create(name="Less Awesome Loot", dkp=25)
        Event.objects.create(name="Awesome Event")

    def test_raid_loot(self):
        raid = Raid.objects.create(
            event=Event.objects.get(name="Awesome Event"),
            date=datetime.datetime.now().date(),
            attendance_value=1,
        )
        Loot.objects.create(item=Item.objects.get(name="Awesome Loot"), raid=raid)
        Loot.objects.create(item=Item.objects.get(name="Less Awesome Loot"), raid=raid)
        Loot.objects.create(item=Item.objects.get(name="Less Awesome Loot"), raid=raid)

        self.assertEqual(len(raid.loot()), 3)

    def test_raid_dkp_value(self):
        raid = Raid.objects.create(
            event=Event.objects.get(name="Awesome Event"),
            date=datetime.datetime.now().date(),
            attendance_value=1,
        )
        Loot.objects.create(
            item=Item.objects.get(name="Awesome Loot"),
            raid=raid,
            dkp=Item.objects.get(name="Awesome Loot").dkp,
        )
        Loot.objects.create(
            item=Item.objects.get(name="Less Awesome Loot"),
            raid=raid,
            dkp=Item.objects.get(name="Less Awesome Loot").dkp,
        )
        Loot.objects.create(
            item=Item.objects.get(name="Less Awesome Loot"),
            raid=raid,
            dkp=Item.objects.get(name="Less Awesome Loot").dkp,
        )

        dkp = raid.dkp()

        self.assertIsInstance(dkp, float)
        self.assertEqual(dkp, 100.0)

    def test_dkp_per_person_with_no_raiders(self):
        raid = Raid.objects.create(
            event=Event.objects.get(name="Awesome Event"),
            date=datetime.datetime.now().date(),
            attendance_value=1,
        )

        self.assertEqual(raid.dkp_per_person(), 0.0)


class RaiderTestCase(TestCase):
    def setUp(self):
        characters = CharacterFactory()
        characters.create_batch(10)

    def test_character_factory(self):
        assert len(Character.objects.get()) == 10
