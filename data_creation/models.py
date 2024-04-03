from django.db import models


# Create your models here.

class Event(models.Model):
    event_name = models.CharField(max_length=100)
    city_name = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.event_name
