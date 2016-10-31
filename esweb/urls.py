from django.conf.urls import include, url
from django.contrib import admin

admin.site.site_header = 'Eternal Sovereign Administration'

urlpatterns = [
    # Examples:
    # url(r'^$', 'esweb.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', admin.site.urls),
    url(r'^roster/', include('roster.urls', namespace="roster")),
]
