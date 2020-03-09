from django.db import models


class Planet(models.Model):
    name = models.CharField(max_length=30)
    period = models.FloatField()                            # Period of a planet in years.
    diameter = models.IntegerField()                        # Diameter of a planet in kilometers.
    mass = models.FloatField()                              # Mass of a planet in Earth masses.
    have_satellites = models.BooleanField(default=False)    # Boolean value describing if planet has natural satellites.

    def __str__(self):
        return self.name
