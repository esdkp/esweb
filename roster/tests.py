from django.test import TestCase
from .models import EQClass, EQRace, EQCharacter
from .constants import EQ_CHARACTER_NAME_MINIMUM_LENGTH


class EQClassTestCase(TestCase):
    def test_class_must_have_both_short_and_long_name(self):
        eqclass = EQClass()
        self.assertFalse(eqclass.name == None)
        self.assertFalse(eqclass.short_name == None)


class EQRaceTestCase(TestCase):
    def test_race_must_have_both_short_and_long_name(self):
        eqrace = EQRace()
        self.assertFalse(eqrace.name == None)
        self.assertFalse(eqrace.short_name == None)


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
        eqclass = EQClass.objects.create()
        eqrace = EQRace.objects.create()
        names = ["Alsmack", "Kazh", "Ylyrra"]
        for name in names:
            EQCharacter.objects.create(name=name, eqclass=eqclass, eqrace=eqrace)

        response = self.client.get('/roster/')
        for name in names:
            self.assertContains(response, name)

