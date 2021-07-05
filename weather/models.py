from django.contrib.gis.db.models import PointField
from django.db import models

# Create your models here.

class Location(models.Model):
    name = models.CharField(max_length=25, null=True)
    point = PointField()

    def __str__(self):
        return str(self.name)

    @property
    def lat_lon(self):
        return list(getattr(self.point, 'coords', []) [::-1])