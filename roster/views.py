from django.views import generic
from django.shortcuts import get_object_or_404
from eq.models import Character, Guild


class RosterView(generic.ListView):
    model = Character
    template_name = "roster/index.html"
    context_object_name = "characters"


class CharacterView(generic.DetailView):
    model = Character
    template_name = "roster/character_detail.html"
    context_object_name = "character"


class GuildsView(generic.ListView):
    model = Guild
    template_name = "roster/guilds.html"
    context_object_name = "guilds"


class GuildRosterView(generic.DetailView):
    model = Guild
    template_name = "roster/guild.html"
    context_object_name = "guild"
