from django.conf.urls import url

from roster import views

app_name = 'roster'
urlpatterns = [
    url(r'^$', views.RosterView.as_view(), name='index'),
    url(r'^(?P<pk>\d+)/$', views.CharacterView.as_view(), name='character'),
]
