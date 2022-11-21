from django.contrib import admin
from django.utils.html import format_html

from adminsortable2.admin import SortableTabularInline, SortableAdminMixin, SortableAdminBase, SortableInlineAdminMixin

from .models import Place, Image



class ImageInline(SortableTabularInline, admin.TabularInline):
    model = Image
    readonly_fields = ("preview_image", )
    fields = ["upload", "preview_image"]

    def preview_image(self, model):
        return format_html(
            f"<img src='{model.upload.url}' height='200px' />"
        )

@admin.register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]
    

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    pass
