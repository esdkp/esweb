from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path
from rest_framework import routers
import eq.views

admin.site.site_header = "Eternal Sovereign Administration"
router = routers.DefaultRouter()
router.register(r"characters", eq.views.CharacterViewSet)

urlpatterns = [
    url(r"^admin/", admin.site.urls),
    url(r"^roster/", include("roster.urls", namespace="roster")),
    url(r"^dkp/", include("dkp.urls", namespace="dkp")),
    path("api/", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]
