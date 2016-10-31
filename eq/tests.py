from django.test import TestCase
from .models import Klass, Race, Expansion


class KlassTestCase(TestCase):
    def test_class_must_have_both_short_and_long_name(self):
        eqclass = Klass()
        self.assertFalse(eqclass.name == None)
        self.assertFalse(eqclass.short_name == None)


class RaceTestCase(TestCase):
    def test_race_must_have_both_short_and_long_name(self):
        eqrace = Race()
        self.assertFalse(eqrace.name == None)
        self.assertFalse(eqrace.short_name == None)


class ExpansionTestCase(TestCase):
    def test_expansion_must_have_both_short_and_long_name(self):
        expansion = Expansion()
        self.assertFalse(expansion.name == None)
        self.assertFalse(expansion.short_name == None)
