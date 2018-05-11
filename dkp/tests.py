import datetime

from django.test import TestCase
from eq.models import Item, Event
from .models import Loot, Raid


class RaidTestCase(TestCase):
    def setUp(self):
        Item.objects.create(name="Awesome Loot", dkp=50)
        Item.objects.create(name="Less Awesome Loot", dkp=25)
        Event.objects.create(name="Awesome Event")

    def TestDKPValue(self):
        raid = Raid.objects.create(event=Event.objects.get(name="Awesome Event"), date=datetime.datetime.now().date())
        Loot.objects.create(item=Item.objects.get(name="Awesome Loot"), raid=raid)
        Loot.objects.create(item=Item.objects.get(name="Less Awesome Loot"), raid=raid)
        Loot.objects.create(item=Item.objects.get(name="Less Awesome Loot"), raid=raid)

        self.assertEqual(raid.dkp(), 100)
        self.assertFalse(True)
