from django.db import models


class EQClass(models.Model):
    name = models.TextField()
    short_name = models.TextField()


class EQRace(models.Model):
    name = models.TextField()
    short_name = models.TextField()


class EQCharacter(models.Model):
    name = models.TextField()
    surname = models.TextField()
    eqclass = models.ForeignKey(EQClass)
    eqrace = models.ForeignKey(EQRace)
