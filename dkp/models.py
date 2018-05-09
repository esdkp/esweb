from django.db import models
from eq.models import Event, Item


class Raid(models.Model):
    date = models.DateTimeField()
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    attendance_value = models.FloatField()

    def loot(self):
        return Loot.objects.filter(raid=self.id)

    # The amount of DKP the raid is worth.
    def dkp(self):
        return sum([l.dkp for l in self.loot()])

    def __str__(self):
        return "{} {}".format(self.date, self.event.name)


class Loot(models.Model):
    raid = models.ForeignKey(Raid, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    dkp = models.FloatField()  # The amount of DKP the item was sold for

    def __str__(self):
        return "{} {}".format(self.raid, self.item)
