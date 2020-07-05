"""
Views for EQ app
"""
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from .models import Character, Expansion, Guild, Klass, Race, Server, Event
from .serializers import (
    CharacterSerializer,
    ExpansionSerializer,
    GuildSerializer,
    KlassSerializer,
    RaceSerializer,
    ServerSerializer,
    EventSerializer,
)


class CharacterViewSet(viewsets.ModelViewSet):
    """
    API endpoint for characters in the eq database
    """

    queryset = Character.objects.all()
    serializer_class = CharacterSerializer


class ExpansionViewSet(viewsets.ModelViewSet):
    """
    API endpoint for expansions in the eq database
    """

    queryset = Expansion.objects.all()
    serializer_class = ExpansionSerializer


class GuildViewSet(viewsets.ModelViewSet):
    """
    API endpoint for expansions in the eq database
    """

    queryset = Guild.objects.all()
    serializer_class = GuildSerializer


class KlassViewSet(viewsets.ModelViewSet):
    """
    API endpoint for classes in the eq database
    """

    queryset = Klass.objects.all()
    serializer_class = KlassSerializer


class RaceViewSet(viewsets.ModelViewSet):
    """
    API endpoint for classes in the eq database
    """

    queryset = Race.objects.all()
    serializer_class = RaceSerializer


class ServerViewSet(viewsets.ModelViewSet):
    """
    API endpoint for classes in the eq database
    """

    queryset = Server.objects.all()
    serializer_class = ServerSerializer


class EventViewSet(viewsets.ModelViewSet):
    """
    API endpoint for classes in the eq database
    """

    queryset = Event.objects.all()
    serializer_class = EventSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["expansion"]
