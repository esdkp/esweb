"""
Django Admin site configuration for DKP app
"""
from django.contrib import admin
from . import models


admin.site.register(models.Raid)
admin.site.register(models.Loot)
