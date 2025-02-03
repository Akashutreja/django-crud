from django.db import models

class UserData(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    coordinates_latitude = models.FloatField(null=True, blank=True)
    coordinates_longitude = models.FloatField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
