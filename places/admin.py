from django.contrib import admin
from django.utils.html import format_html

from .models import Place, Image

class ImageInline(admin.TabularInline):
    model = Image
    readonly_fields = ("preview_image", )

    def preview_image(self, model):
        return format_html(
            f"<img src='{model.upload.url}' height='200px' />"
        )

@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = (
        "title",
    )
    inlines = [
        ImageInline,
    ]

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    pass
