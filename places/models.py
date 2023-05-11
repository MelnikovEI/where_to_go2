from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField(max_length=200)
    description_short = models.TextField(verbose_name='краткое описание', blank=True)
    description_long = HTMLField(verbose_name='подробное описание', blank=True)
    lng = models.FloatField()
    lat = models.FloatField()

    class Meta:
        unique_together = ['title', 'lng', 'lat']

    def __str__(self):
        return self.title


class Image(models.Model):
    place = models.ForeignKey(Place, related_name='images', on_delete=models.CASCADE, null=True)
    order = models.PositiveIntegerField(verbose_name='позиция', default=0, db_index=True)
    img = models.ImageField()

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.img.name
