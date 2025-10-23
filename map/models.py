from django.db import models
from django.conf import settings
from django.utils import timezone

# модель для хранения мест 
class Places(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) # кто выложил место
    title = models.CharField(max_length=200) # заголовок места
    description_short = models.TextField(blank=True) # описания
    description_long = models.TextField(blank=True)
    lng = models.DecimalField(max_digits=20, decimal_places=15, default=0)  # долгота
    lat = models.DecimalField(max_digits=20, decimal_places=15, default=0)  # широта
    created_date = models.DateTimeField(default=timezone.now) # когда создана запись

    def __str__(self):
        return self.title

# модель для хранения картинок из мест
class PlaceImage(models.Model):
    place = models.ForeignKey(Places, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='places/')
    order = models.PositiveIntegerField(default=0)  # для порядка изображений

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"Image for {self.place.title}"