"""
Views for EQ app
"""
from rest_framework import viewsets
from .models import Character
from .serializers import CharacterSerializer


class CharacterViewSet(viewsets.ModelViewSet):
    """
    API endpoint for characters in the eq database
    """

    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
