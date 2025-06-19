from django.contrib import admin
from .models import MobileTower
from leaflet.admin import LeafletGeoAdmin

@admin.register(MobileTower)
class MobileTowerAdmin(LeafletGeoAdmin):
    list_display = ("mno", "code", "location")
