import datetime
import pytest
from rest_framework.test import APIClient
from dkp.models import Loot, Raid

from eq.models import Event, Item


@pytest.fixture
def api_client() -> APIClient:
    return APIClient()


@pytest.fixture()
def items(db):
    Item.objects.create(name="Awesome Loot", dkp=50)
    Item.objects.create(name="Less Awesome Loot", dkp=25)


@pytest.fixture
def event(db):
    Event.objects.create(name="Awesome Event")


@pytest.fixture
def raid(db, event, items):
    raid = Raid.objects.create(
        event=Event.objects.get(name="Awesome Event"),
        date=datetime.datetime.now().date(),
        attendance_value=1,
    )
    Loot.objects.create(item=Item.objects.get(name="Awesome Loot"), raid=raid)
    Loot.objects.create(item=Item.objects.get(
        name="Less Awesome Loot"), raid=raid)
    Loot.objects.create(item=Item.objects.get(
        name="Less Awesome Loot"), raid=raid)
    return raid