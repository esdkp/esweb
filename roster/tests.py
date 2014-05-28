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