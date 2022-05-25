from django.conf.urls import include
from django.contrib import admin
from django.urls import path, re_path
from rest_framework import routers
import eq.views
import dkp.views

admin.site.site_header = "Eternal Sovereign DKP Administration"
router = routers.DefaultRouter()
router.register(r"characters", eq.views.CharacterViewSet)
router.register(r"classes", eq.views.KlassViewSet)
router.register(r"expansions", eq.views.ExpansionViewSet)
router.register(r"guilds", eq.views.GuildViewSet)
router.register(r"races", eq.views.RaceViewSet)
router.register(r"servers", eq.views.ServerViewSet)
router.register(r"events", eq.views.EventViewSet)
router.register(r"items", eq.views.ItemViewSet)
router.register(r"raids", dkp.views.RaidViewSet)
router.register(r"loots", dkp.views.LootViewSet)
router.register(r"raiders", dkp.views.RaiderViewSet)

urlpatterns = [
    re_path(r"^admin/", admin.site.urls),
    re_path(r"^roster/", include("roster.urls", namespace="roster")),
    re_path(r"^dkp/", include("dkp.urls", namespace="dkp")),
    path("api/", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]
