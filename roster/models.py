from django.db import models


class EQClass(models.Model):
    name = models.TextField()
    short_name = models.TextField()

    def __str__(self):
        return self.name


class EQRace(models.Model):
    name = models.TextField()
    short_name = models.TextField()

    def __str__(self):
        return self.name


class EQCharacter(models.Model):
    name = models.TextField()
    surname = models.TextField(blank=True)
    eqclass = models.ForeignKey(EQClass)
    eqrace = models.ForeignKey(EQRace)

    def __str__(self):
        return self.name
