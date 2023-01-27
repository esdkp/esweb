import pytest

from rest_framework.test import APIClient

from dkp.models import Raid
from dkp.serializers import RaidSerializer


class TestImportView:

    @staticmethod
    @pytest.mark.django_db
    def test_it_works(api_client: APIClient, raid: Raid):
        resp = api_client.get(f'/api/raids/{raid.event_id}', follow=True)
        expected = RaidSerializer(raid).data
        actual = resp.json()
        assert actual == expected
