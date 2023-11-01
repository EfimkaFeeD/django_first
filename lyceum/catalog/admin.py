__all__ = ["ItemAdmin", "ImagesAdmin"]

from django.contrib import admin

import catalog.models


class ImagesInline(admin.StackedInline):
    model = catalog.models.Images


class MainImageInline(admin.StackedInline):
    model = catalog.models.MainImage


@admin.register(catalog.models.Images)
class ImagesAdmin(admin.ModelAdmin):
    list_display = (catalog.models.Images.image_tmb,)


@admin.register(catalog.models.Item)
class ItemAdmin(admin.ModelAdmin):
    inlines = [ImagesInline, MainImageInline]
    list_display = (
        catalog.models.Item.name.field.name,
        catalog.models.Item.is_published.field.name,
    )
    list_editable = (catalog.models.Item.is_published.field.name,)
    list_display_links = (catalog.models.Item.name.field.name,)
    filter_horizontal = (catalog.models.Item.tags.field.name,)


admin.site.register(catalog.models.Tag)
admin.site.register(catalog.models.Category)
