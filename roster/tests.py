from unittest import skip
from django.test import TestCase
from .models import EQCharacter
from .constants import EQ_CHARACTER_NAME_MINIMUM_LENGTH

import eq.models


# TODO: All these assert false thing == None tests are useless
# Figure out how to ensure that only properly formatted data
# can end up in the DB.
class EQCharacterTestCase(TestCase):
    def test_character_must_have_name(self):
        character = EQCharacter()
        self.assertFalse(character.name == None)

    def test_character_name_minimum_length(self):
        character = EQCharacter(name="Awesomenaut")
        self.assertGreater(len(character.name), EQ_CHARACTER_NAME_MINIMUM_LENGTH)


class RosterViewTestCase(TestCase):
    def test_roster_view_uses_template(self):
        response = self.client.get('/roster/')
        self.assertTemplateUsed('roster_view.html')

    def test_roster_lists_characters(self):
        eqclass = eq.models.Klass.objects.create()
        eqrace = eq.models.Race.objects.create()
        names = ["Alsmack", "Kazh", "Ylyrra"]
        for name in names:
            EQCharacter.objects.create(name=name, eqclass=eqclass, eqrace=eqrace)

        response = self.client.get('/roster/')
        for name in names:
            self.assertContains(response, name)
