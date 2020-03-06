from django.db import models


class Planet(models.Model):
    name = models.CharField(max_length=30)
    period = models.IntegerField()
    diameter = models.IntegerField()
    mass = models.IntegerField()
    have_satellites = models.BooleanField()
