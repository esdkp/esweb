"""
DKP Views
"""
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView

from .models import Raid
from .forms import RaidCreateForm


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
        response["Last-Modified"] = latest_raid.date.strftime("%a, %d %b %Y %H:%M:%S GMT")
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
