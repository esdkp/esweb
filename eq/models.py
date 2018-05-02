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

    def characters(self):
        return Character.objects.filter(guild=self.id)

    def __str__(self):
        return self.name


class Character(models.Model):
    name = models.TextField(unique=True)
    surname = models.TextField(blank=True)
    eqclass = models.ForeignKey(Klass, on_delete=models.CASCADE)
    eqrace = models.ForeignKey(Race, on_delete=models.CASCADE)
    eqflags = models.ManyToManyField(Flag, blank=True)
    guild = models.ForeignKey(Guild, blank=True, null=True, on_delete=models.CASCADE)
    server = models.ForeignKey(Server, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Character'
        verbose_name_plural = 'Characters'

    def __str__(self):
        return self.name


class Event(models.Model):
    name = models.TextField()
    expansion = models.ForeignKey(Expansion, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.TextField()
    event = models.ForeignKey(Event, on_delete=models.CASCADE, blank=True, null=True)
    expansion = models.ForeignKey(Expansion, on_delete=models.CASCADE, blank=True, null=True)
    default_value = models.FloatField(default=0)

    def get_expansion(self):
        if self.expansion is not None:
            return self.expansion.short_name
        elif event is not None:
            return self.event.expansion.short_name
        else:
            return None

    def full_name(self):
        e = self.get_expansion()
        if e is not None:
            return "[{}] {}".format(e, self.name)
        else:
            return self.name

    def __str__(self):
        return self.full_name
