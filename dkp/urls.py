"""
URLs for DKP app
"""
from django.urls import path, re_path
from . import views

app_name = "dkp"

urlpatterns = [
    re_path(r"^$", views.RaidsView.as_view(), name="index"),
    path("raids/add/", views.RaidCreateView.as_view(), name="raid-add"),
    path("raids/<pk>/", views.RaidDetailView.as_view(), name="raid-view"),
]
