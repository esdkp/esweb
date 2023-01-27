from rest_framework.test import APIClient

from dkp.models import Raid
from dkp.serializers import RaidSerializer


class TestImportView:
    endpoint = '/api/import/'

    @staticmethod
    def test_mike_understands_the_fixture_setup(authenticated_client: APIClient, raid: Raid):
        resp = authenticated_client.get(f'/api/raids/{raid.event_id}', follow=True)
        expected = RaidSerializer(raid).data
        actual = resp.json()
        assert actual == expected

    def test_import_smoke(self, authenticated_client: APIClient):
        resp = authenticated_client.post(self.endpoint, {'hello': 'world'})
        assert resp.json() == {'greeting': 'hello'}