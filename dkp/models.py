from django.db import models
from eq.models import Event, Item, Character


class Raid(models.Model):
    date = models.DateField()
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    attendance_value = models.FloatField()

    def loot(self):
        return Loot.objects.filter(raid=self.id)

    def raiders(self):
        return Raider.objects.filter(raid=self.id)

    # The amount of DKP the raid is worth.
    def dkp(self):
        return float(sum([l.dkp for l in self.loot()]))

    def dkp_per_person(self):
        number_of_raiders = len(self.raiders())
        if number_of_raiders == 0:
            return 0.0

        return self.dkp() / number_of_raiders

    def __str__(self):
        return "{} {}".format(self.date, self.event.name)


class Loot(models.Model):
    raid = models.ForeignKey(Raid, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    # The amount of DKP the item was sold for
    dkp = models.FloatField(default=0)
    # The character that won the item; if blank, item rotted and DKP should be zero probably?
    character = models.ForeignKey(Character, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return "{} {}".format(self.raid, self.item)


class Raider(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    raid = models.ForeignKey(Raid, on_delete=models.CASCADE)
    loot = models.ManyToManyField(Loot)

    def spent(self):
        return sum([l.dkp for l in self.loot])

    def dkp(self):
        return self.raid.dkp() - self.spent()

    def __str__(self):
        return self.character.name
