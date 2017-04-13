from django.shortcuts import render
from django.views import generic
import eq.models


class RosterView(generic.ListView):
    model = eq.models.Character
    template_name = 'roster/index.html'
    context_object_name = 'characters'


class CharacterView(generic.DetailView):
    model = eq.models.Character
    template_name = 'roster/character_detail.html'
    context_object_name = 'character'


class GuildsView(generic.ListView):
    model = eq.models.Guild
    template_name = 'roster/guilds.html'
    context_object_name = 'guilds'


class GuildRosterView(generic.DetailView):
    model = eq.models.Guild
    template_name = 'roster/guild.html'
    context_object_name = 'guild'
