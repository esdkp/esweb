from django.db import models
import eq.models

class EQCharacter(models.Model):
    name = models.TextField(unique=True)
    surname = models.TextField(blank=True)
    eqclass = models.ForeignKey(eq.models.Klass, on_delete=models.CASCADE)
    eqrace = models.ForeignKey(eq.models.Race, on_delete=models.CASCADE)
    eqflags = models.ManyToManyField(eq.models.Flag, blank=True)

    class Meta:
        verbose_name = 'Character'
        verbose_name_plural = 'Characters'

    def __str__(self):
        return self.name
