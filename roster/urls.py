from django.conf.urls import patterns, url

from roster import views

urlpatterns = patterns('',
    url(r'^$', views.RosterView.as_view(), name='index'),
    url(r'^(?P<pk>\d+)/$', views.CharacterView.as_view(), name='character'),
)
