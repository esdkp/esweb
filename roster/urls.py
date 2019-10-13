from django.conf.urls import url
from django.urls import path

from roster import views

app_name = "roster"
urlpatterns = [
    url(r"^$", views.RosterView.as_view(), name="index"),
    url(r"^(?P<pk>\d+)/$", views.CharacterView.as_view(), name="character"),
    path("guilds/", views.GuildsView.as_view(), name="guilds"),
    path("guild/<pk>/", views.GuildRosterView.as_view(), name="guild"),
]
