"""
URLs for DKP app
"""
from django.conf.urls import url
from django.urls import path
from . import views

app_name = "dkp"

urlpatterns = [
    url(r"^$", views.RaidsView.as_view(), name="index"),
    path("raids/add/", views.RaidCreateView.as_view(), name="raid-add"),
    path("raids/<pk>/", views.RaidDetailView.as_view(), name="raid-view"),
]
