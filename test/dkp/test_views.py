from rest_framework.test import APIClient

from dkp.models import Raid
from dkp.serializers import RaidSerializer


class TestImportView:
    endpoint = '/api/import/'

    @staticmethod
    def test_mike_understands_the_fixture_setup(api_client: APIClient, raid: Raid):
        resp = api_client.get(f'/api/raids/{raid.event_id}', follow=True)
        expected = RaidSerializer(raid).data
        actual = resp.json()
        assert actual == expected

    def test_import_smoke(self, api_client: APIClient):
        resp = api_client.post(self.endpoint, {'hello': 'world'})
        assert resp.json() == {'greeting': 'hello'}