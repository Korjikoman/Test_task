from django.db import models
from django.conf import settings
from django.utils import timezone

class Places(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description_short = models.TextField(blank=True)
    description_long = models.TextField(blank=True)
    lng = models.DecimalField(max_digits=9, decimal_places=6, default=-1)  # долгота
    lat = models.DecimalField(max_digits=9, decimal_places=6, default=-1)  # широта
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

class PlaceImage(models.Model):
    place = models.ForeignKey(Places, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='places/')
    order = models.PositiveIntegerField(default=0)  # для порядка изображений

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"Image for {self.place.title}"