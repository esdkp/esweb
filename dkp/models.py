from django.db import models
from eq.models import Event, Item


class Raid(models.Model):
	date = models.DateTimeField()
	event = models.ForeignKey(Event, on_delete=models.CASCADE)
	attendance_value = models.FloatField()

	def loot(self):
		return Loot.objects.filter(raid = self.id)

	def __str__(self):
		return "{} {}".format(self.date, self.event.name)



class Loot(models.Model):
	raid = models.ForeignKey(Raid, on_delete=models.CASCADE)
	item = models.ForeignKey(Item, on_delete=models.CASCADE)
	dkp_value = models.FloatField()

	def __str__(self):
		return "{} {}".format(self.raid, self.item)
