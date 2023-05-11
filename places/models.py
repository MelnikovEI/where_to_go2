from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField(max_length=200)
    description_short = models.CharField(max_length=500)
    description_long = HTMLField(blank=True)
    lng = models.FloatField(null=True)
    lat = models.FloatField(null=True)

    def __str__(self):
        return self.title

    class Meta:
        unique_together = ['title', 'lng', 'lat']


class Image(models.Model):
    place = models.ForeignKey(Place, related_name='images', on_delete=models.CASCADE, null=True)
    order = models.PositiveIntegerField(verbose_name='позиция', null=False, blank=False, default=0, db_index=True)
    img = models.ImageField()

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.img.name
