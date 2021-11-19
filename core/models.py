from django.db import models

# Create your models here.
class Geolocations(models.Model):
    city = models.CharField(max_length=40)
    country = models.CharField(max_length=40)
    latitude = models.FloatField()
    longitude = models.FloatField(max_length=30)
    longitude = models.CharField(max_length=30)
    duration = models.CharField(max_length=40)
    place = models.CharField(max_length=40)
    date = models.DateField()
    class Meta:
        verbose_name_plural = "Geolocations"
    def __str__(self):
        return f"There will be a planned power interruption on {self.date} at {self.place} between {self.duration}"