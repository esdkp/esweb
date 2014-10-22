from django.shortcuts import render
from django.views import generic
from roster.models import EQCharacter, EQRace, EQClass


class RosterView(generic.ListView):
    template_name = 'roster/listing.html'
    context_object_name = 'characters'

    def get_queryset(self):
        return EQCharacter.objects.all()
