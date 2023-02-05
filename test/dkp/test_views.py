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

    def test_import_smoke(self, authenticated_client: APIClient, sample_import_data):
        resp = authenticated_client.post(self.endpoint, { 'loots': sample_import_data['Loots'] }, format='json',)
        assert resp.json() == {'greeting': 'hello'}

    # failure/partial failure cases
    def test_it_fails_completely_if_raid_already_exists(self,authenticated_client: APIClient):
        pass
    
    def test_it_reports_if_some_items_already_exist(self,authenticated_client: APIClient):
        pass

    def test_it_reports_if_some_characters_already_exist(self,authenticated_client: APIClient):
        pass

    # happy path
    # NOTE: might create more specific test cases as I discover what "appropriately" means in more detail
    def test_it_creates_a_raid_and_event_appropriately(self, authenticated_client: APIClient):
        pass

    def test_it_updates_characters_and_raiders_appropriately(self, authenticated_client: APIClient):
        pass