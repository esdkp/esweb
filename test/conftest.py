import datetime
import pytest
from rest_framework.test import APIClient
from dkp.models import Loot, Raid
from pathlib import Path
from eq.models import Event, Item
import json

# @pytest.fixture(scope='session')
# def seed_db(django_db_setup, django_db_blocker):
#     """use fixtures mentioned in README in tests"""
#     with django_db_blocker.unblock():
#         call_command('loaddata', 'classes', 'events', 'expansions', 'races', 'servers')

DIRECTORY = Path(__file__).parent
RESOURCE_DIR = DIRECTORY.joinpath('resources')

@pytest.fixture
def sample_import_data():
    with RESOURCE_DIR.joinpath('sample-import-request.json').open() as f:
        yield json.load(f)

@pytest.fixture
def test_user(django_user_model):
    return django_user_model.objects.create(username='bilbo_baggins', password='hunter2')

@pytest.fixture
def authenticated_client(test_user) -> APIClient:
    client = APIClient()
    client.force_login(test_user)
    yield client
    client.logout()


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