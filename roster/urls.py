from django.conf.urls import url

from roster import views

app_name = 'roster'
urlpatterns = [
    url(r'^$', views.RosterView.as_view(), name='index'),
    url(r'^(?P<pk>\d+)/$', views.CharacterView.as_view(), name='character'),
    url(r'^guilds/$', views.GuildsView.as_view(), name='guilds'),
    url(r'^guild/(?P<pk>\d+)/$', views.GuildRosterView.as_view(), name='guild'),
]
