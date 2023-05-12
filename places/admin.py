from django.contrib import admin
from django.utils.html import format_html
from adminsortable2.admin import SortableInlineAdminMixin

from .models import Place, Image


class ImageInline(SortableInlineAdminMixin, admin.StackedInline):
    model = Image

    @staticmethod
    def preview_img(image: Image):
        return format_html(
            '<img src="{}" width="{}" height={} />',
            image.img.url,
            image.img.width / (image.img.height / 200),
            200,
        )

    readonly_fields = ['preview_img']
    fields = ('img', 'preview_img', 'order')


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]
    search_fields = ['title']


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    pass
