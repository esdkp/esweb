from unittest import skip
from django.test import TestCase

import eq.models


class RosterViewTestCase(TestCase):
    fixtures = ["classes.yaml", "races.yaml", "servers.yaml"]

    def test_roster_view_uses_template(self):
        response = self.client.get('/roster/')
        self.assertTemplateUsed('roster_view.html')

    def test_roster_lists_characters(self):
        eqclass = eq.models.Klass.objects.get(id=1)
        eqrace = eq.models.Race.objects.get(id=1)
        eqserver = eq.models.Server.objects.get(id=1)
        names = ["Alsmack", "Kazh", "Ylyrra"]
        for name in names:
            eq.models.Character.objects.create(name=name,
                eqclass=eqclass, eqrace=eqrace, server=eqserver, guild=None)

        response = self.client.get('/roster/')
        for name in names:
            self.assertContains(response, name)

class GuildsViewTestCase(TestCase):
    fixtures = ["servers.yaml"]

    def test_guild_view_uses_template(self):
        response = self.client.get('/roster/guilds/')
        self.assertTemplateUsed('guilds.html')

    def test_guilds_view_lists_guilds(self):
        guild_names = ["Eternal Sovereign", "Rainbow Friends"]
        server = eq.models.Server.objects.get(id=1)
        for name in guild_names:
            eq.models.Guild.objects.create(
                name=name,
                server=server
            )

        response = self.client.get('/roster/guilds/')
        for name in guild_names:
            self.assertContains(response, name)

class GuildViewTestCase(TestCase):
    fixtures = ["servers.yaml"]

    def setUp(self):
        guild_names = ["Eternal Sovereign", "Rainbow Friends", "Enchiladas"]

    def test_guild_view_list_characters_in_guild(self):
        pass
