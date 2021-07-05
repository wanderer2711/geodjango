from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from .models import Location

@admin.register(Location)
class LocationAdmin(OSMGeoAdmin):
    default_lat = 1400000
    default_lon = 7495000
    default_zoom = 12 