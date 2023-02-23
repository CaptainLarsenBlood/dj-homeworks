from django.db import models
from django.utils.timezone import now


class Sensor(models.Model):
    name = models.CharField(max_length=20)
    location = models.CharField(max_length=40)


class Measurement(models.Model):
    temperature = models.DecimalField(max_digits=5, decimal_places=2)
    date = models.DateTimeField(default=now())
    sensors = models.ForeignKey(Sensor, on_delete=models.CASCADE, null=True, related_name='measurements')

