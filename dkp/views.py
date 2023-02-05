"""
DKP Views
"""
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from .models import Raid, Loot, Raider
from .forms import RaidCreateForm
from .serializers import (
    ImportSerializer,
    RaidSerializer,
    LootSerializer,
    RaiderSerializer,
)

class ImportView(viewsets.GenericViewSet):
    """
    API endpoint for bootstrapping a Raid (and optionally, event) with all the necessary character and loot configuration
    
    does it's best to "partially succeed" (instead of "fail fast") while letting the caller know what it can or cannot complete
    """
    serializer_class = ImportSerializer
    
    def create(self, request):
        # service logic stub
        # create raid - should fail entire route if raid with same name already exists
        serializer = ImportSerializer(data=request.data)
        if serializer.is_valid():
            return Response({'greeting': 'hello'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RaidsView(ListView):
    """
    View all raids
    """

    model = Raid
    template_name = "dkp/raid_list.html"
    context_object_name = "raids"

    def head(self):
        """
        Handle HEAD requests, sets Last-Modified to the most recent raid date
        """
        latest_raid = self.get_queryset().latest("date")
        response = HttpResponse("")
        response["Last-Modified"] = latest_raid.date.strftime(
            "%a, %d %b %Y %H:%M:%S GMT"
        )
        return response


class RaidDetailView(DetailView):
    """
    Raid Detail
    """

    model = Raid
    template_name = "dkp/raid_detail.html"
    context_object_name = "raid"


class RaidCreateView(CreateView):
    """
    Create Raid View
    """

    model = Raid
    template_name = "dkp/raid_add.html"
    form_class = RaidCreateForm
    success_url = reverse_lazy("raid-view")



class RaidViewSet(viewsets.ModelViewSet):
    """
    API endpoint for raids in the eq database
    """

    queryset = Raid.objects.all()
    serializer_class = RaidSerializer


class LootViewSet(viewsets.ModelViewSet):
    """
    API endpoint for assigned loot in the eq database
    """

    queryset = Loot.objects.all()
    serializer_class = LootSerializer


class RaiderViewSet(viewsets.ModelViewSet):
    """
    API endpoint for raiders in the eq database
    """

    queryset = Raider.objects.all()
    serializer_class = RaiderSerializer
