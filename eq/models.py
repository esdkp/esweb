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


class Server(models.Model):
    name = models.TextField(unique=True)
    short_name = models.TextField(unique=True)

    def __str__(self):
        return self.name


class Guild(models.Model):
    name = models.TextField(unique=True)
    server = models.ForeignKey(Server, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Character(models.Model):
    name = models.TextField(unique=True)
    surname = models.TextField(blank=True)
    eqclass = models.ForeignKey(Klass, on_delete=models.CASCADE)
    eqrace = models.ForeignKey(Race, on_delete=models.CASCADE)
    eqflags = models.ManyToManyField(Flag, blank=True)
    guild = models.ForeignKey(Guild, blank=True, null=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Character'
        verbose_name_plural = 'Characters'

    def __str__(self):
        return self.name
