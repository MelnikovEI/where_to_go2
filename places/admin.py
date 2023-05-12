from django.contrib import admin
from django.utils.html import format_html
from adminsortable2.admin import SortableInlineAdminMixin

from .models import Place, Image


class ImageInline(SortableInlineAdminMixin, admin.StackedInline):
    model = Image

    @staticmethod
    def img_preview(obj):
        return format_html(
            '<img src="{url}" width="{width}" height={height} />'.format(
                url=obj.img.url,
                width=obj.img.width/(obj.img.height/200),
                height=200,
            )
        )

    readonly_fields = ['img_preview']
    fields = ('img', 'img_preview', 'order')


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]
    search_fields = ['title']


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    pass
