"""
Test factories for EQ models
"""
import factory

from .models import Character


class CharacterFactory(factory.django.DjangoModelFactory):
    """
    Character test factory
    """

    class Meta:
        model = Character

    name = factory.Faker("first_name")
