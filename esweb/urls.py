from django.conf.urls import include, url
from django.contrib import admin

admin.site.site_header = "Eternal Sovereign Administration"

urlpatterns = [
    url(r"^admin/", admin.site.urls),
    url(r"^roster/", include("roster.urls", namespace="roster")),
    url(r"^dkp/", include("dkp.urls", namespace="dkp")),
]
