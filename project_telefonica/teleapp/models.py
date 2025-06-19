from django.contrib.gis.db import models

class MobileTower(models.Model):
    mno = models.CharField(max_length=50)
    code = models.CharField(max_length=100)
    location = models.PointField()  # Geographic point field

    def __str__(self):
        return f"{self.mno} - {self.code}"
