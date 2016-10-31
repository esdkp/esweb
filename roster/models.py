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


class EQExpansion(models.Model):
    name = models.TextField()
    short_name = models.TextField()

    class Meta:
        verbose_name = 'Expansion'

    def __str__(self):
        return self.name


class EQFlag(models.Model):
    name = models.TextField()
    description = models.TextField(blank=True)
    expansion = models.ForeignKey(EQExpansion, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Flag'

    def __str__(self):
        return self.name


class EQCharacter(models.Model):
    name = models.TextField()
    surname = models.TextField(blank=True)
    eqclass = models.ForeignKey(EQClass, on_delete=models.CASCADE)
    eqrace = models.ForeignKey(EQRace, on_delete=models.CASCADE)
    flags = models.ManyToManyField(EQFlag)

    class Meta:
        verbose_name = 'Character'

    def __str__(self):
        return self.name
