import datetime

from django.test import Client, TestCase
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


# class RaiderTestCase(TestCase):
#     def setUp(self):
#         characters = CharacterFactory()
#         characters.create_batch(10)

#     def test_character_factory(self):
#         assert len(Character.objects.get()) == 10

class ImportViewTestCase(TestCase):
    def setUp(self):
        # We don't actually want to create anythings, import should do that for us
        # Item.objects.create(name="Awesome Loot", dkp=50)
        # Item.objects.create(name="Less Awesome Loot", dkp=25)
        # Event.objects.create(name="Awesome Event")
        self.c = Client()

    def test_import_view_works_with_no_data_in_database(self):
        data = {
            "date": datetime.datetime.now().date(),
            "name": "Awesome Event",
            "attendance": 1,
            "raiders": ["Awesome Raider"],
            "loots": [
                {"name": "Awesome Loot", "points": 50},
                {"name": "Less Awesome Loot", "points": 25},
            ],
        }
        response = self.c.post("/dkp/import/", data, format="json")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Raid.objects.count(), 1)
        self.assertEqual(Event.objects.count(), 1)
        self.assertEqual(Loot.objects.count(), 2)
        self.assertEqual(Character.objects.count(), 1)
        self.assertEqual(Character.objects.get().name, "Awesome Raider")
        self.assertEqual(Item.objects.count(), 2)
        self.assertEqual(Item.objects.get(name="Awesome Loot").dkp, 50)
        self.assertEqual(Item.objects.get(name="Less Awesome Loot").dkp, 25)