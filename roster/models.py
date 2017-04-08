from __future__ import unicode_literals
from django.db import models
import eq.models


class Person(models.Model):
    characters = models.ManyToManyField(eq.models.Character, blank=True)

    class Meta:
        verbose_name = 'Person'
        verbose_name_plural = 'People'
