from django.urls import path, re_path

from roster import views

app_name = "roster"
urlpatterns = [
    re_path(r"^$", views.RosterView.as_view(), name="index"),
    re_path(r"^(?P<pk>\d+)/$", views.CharacterView.as_view(), name="character"),
    path("guilds/", views.GuildsView.as_view(), name="guilds"),
    path("guild/<pk>/", views.GuildRosterView.as_view(), name="guild"),
]
