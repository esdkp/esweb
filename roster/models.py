from django.db import models


class EQClass(models.Model):
    name = models.TextField()
    short_name = models.TextField()

    class Meta:
        verbose_name = 'Class'
        verbose_name_plural = 'Classes'

    def __str__(self):
        return self.name


class EQRace(models.Model):
    name = models.TextField()
    short_name = models.TextField()

    class Meta:
        verbose_name = 'Race'

    def __str__(self):
        return self.name


class EQCharacter(models.Model):
    name = models.TextField()
    surname = models.TextField(blank=True)
    eqclass = models.ForeignKey(EQClass)
    eqrace = models.ForeignKey(EQRace)

    class Meta:
        verbose_name = 'Character'

    def __str__(self):
        return self.name
