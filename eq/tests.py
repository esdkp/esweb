"""
Unit Tests for EQ app
"""
from django.test import TestCase
from .models import Klass, Race, Expansion, Character
from .constants import CHARACTER_NAME_MINIMUM_LENGTH


# TODO: All these assert false thing == None tests are useless
# Figure out how to ensure that only properly formatted data
# can end up in the DB.


class KlassTestCase(TestCase):
    """
    Klass tests
    """

    def test_class_must_have_both_short_and_long_name(self):
        """
        Klass should not be valid unless it has both the short and long name
        """
        eqclass = Klass()
        self.assertFalse(eqclass.name is None)
        self.assertFalse(eqclass.short_name is None)


class RaceTestCase(TestCase):
    """
    Race tests
    """

    def test_race_must_have_both_short_and_long_name(self):
        """
        Race should not be valid unless it has both the short and long name
        """
        eqrace = Race()
        self.assertFalse(eqrace.name is None)
        self.assertFalse(eqrace.short_name is None)


class ExpansionTestCase(TestCase):
    """
    Expansion tests
    """

    def test_expansion_must_have_both_short_and_long_name(self):
        """
        Expansion should not be valid unless it has both the short and long name
        """
        expansion = Expansion()
        self.assertFalse(expansion.name is None)
        self.assertFalse(expansion.short_name is None)


class CharacterTestCase(TestCase):
    """
    Character tests
    """

    def test_character_must_have_name(self):
        """
        Characters must have a name
        """
        character = Character()
        self.assertFalse(character.name is None)

    def test_character_name_minimum_length(self):
        """
        Character names have to be greater than or equal to EQ's minimum length
        """
        character = Character(name="Awesomenaut")
        self.assertGreater(len(character.name), CHARACTER_NAME_MINIMUM_LENGTH)
