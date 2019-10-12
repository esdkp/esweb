"""
Test factories for DKP models
"""
import factory


class RaiderFactory(factory.django.DjangoModelFactory):
    """
    Raider test factory
    """

    class Meta:
        model = "dkp.models.Raider"


class RaidFactory(factory.django.DjangoModelFactory):
    """
    Raid test factory
    """

    class Meta:
        model = "dkp.models.Raid"


class LootFactory(factory.django.DjangoModelFactory):
    """
    Loot test factory
    """

    class Meta:
        model = "dkp.models.Loot"
