from unittest import skip
from django.test import TestCase

import eq.models


class RosterViewTestCase(TestCase):
    def test_roster_view_uses_template(self):
        response = self.client.get('/roster/')
        self.assertTemplateUsed('roster_view.html')

    def test_roster_lists_characters(self):
        eqclass = eq.models.Klass.objects.create()
        eqrace = eq.models.Race.objects.create()
        names = ["Alsmack", "Kazh", "Ylyrra"]
        for name in names:
            eq.models.Character.objects.create(name=name,
                eqclass=eqclass, eqrace=eqrace, guild=None)

        response = self.client.get('/roster/')
        for name in names:
            self.assertContains(response, name)
