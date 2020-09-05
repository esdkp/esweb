"""
Models specific to the DKP model
"""
from django.db import models
from eq.models import Event, Item, Character


class Raid(models.Model):
    """
    Raids are instances of running an event that has attendance and potentially loot
    """

    date = models.DateField()
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    attendance_value = models.FloatField()

    def loot(self):
        """
        Return list of all loot objects this raid dropped
        """
        return Loot.objects.filter(raid=self.id)

    def raiders(self):
        """
        Return list of all raiders who attended this raid
        """
        return Raider.objects.filter(raid=self.id)

    def dkp(self):
        """
        Calculates the total amount of DKP the raid is worth
        """
        return float(sum([l.dkp for l in self.loot()]))

    def dkp_per_person(self):
        """
        Calculates the amount of DKP earned per raid attendee
        """
        number_of_raiders = len(self.raiders())
        if number_of_raiders == 0:
            return 0.0

        return self.dkp() / number_of_raiders

    def __str__(self):
        return "{} {}".format(self.date, self.event.name)


class Loot(models.Model):
    """
    Loot is an instance of an item associated with a raid
    """

    raid = models.ForeignKey(Raid, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    # The amount of DKP the item was sold for
    dkp = models.FloatField(default=0)
    # The character that won the item; if blank, item rotted and DKP should be zero probably?
    character = models.ForeignKey(Character, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f"{self.raid} {self.item}"


class Raider(models.Model):
    """
    Raider is an instance of a character who has attended a raid
    """

    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    raid = models.ForeignKey(Raid, on_delete=models.CASCADE)
    loot = models.ManyToManyField(Loot, blank=True, null=True)

    def spent(self):
        """
        Calculate amount DKP spent by a given raider
        """
        return sum([l.dkp for l in self.loot])

    def dkp(self):
        """
        Calculate net DKP earned on this raid
        """
        return self.raid.dkp() - self.spent()

    def __str__(self):
        return f"{self.character.name} - {self.raid}"
