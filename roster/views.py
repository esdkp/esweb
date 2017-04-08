from django.shortcuts import render
from django.views import generic
import eq.models


class RosterView(generic.ListView):
    template_name = 'roster/index.html'
    context_object_name = 'characters'

    def get_queryset(self):
        return eq.models.Character.objects.all()


class CharacterView(generic.DetailView):
    model = eq.models.Character
    template_name = 'roster/character_detail.html'
    context_object_name = 'character'
