from __future__ import unicode_literals
from django.db import models


class Klass(models.Model):
    name = models.TextField()
    short_name = models.TextField(unique=True)

    class Meta:
        verbose_name = 'Class'
        verbose_name_plural = 'Classes'

    def __str__(self):
        return self.name


class Race(models.Model):
    name = models.TextField()
    short_name = models.TextField(unique=True)

    class Meta:
        verbose_name = 'Race'
        verbose_name_plural = 'Races'

    def __str__(self):
        return self.name


class Expansion(models.Model):
    name = models.TextField()
    short_name = models.TextField(unique=True)

    class Meta:
        verbose_name = 'Expansion'
        verbose_name_plural = 'Expansions'

    def __str__(self):
        return self.name


class Flag(models.Model):
    name = models.TextField()
    description = models.TextField(blank=True)
    expansion = models.ForeignKey(Expansion, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Flag'
        verbose_name_plural = 'Flags'

    def __str__(self):
        return self.name
