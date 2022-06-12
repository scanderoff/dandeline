from typing import Sequence

from django.contrib import admin
from django.contrib.admin.options import InlineModelAdmin
from django.db.models import Model
from django.utils.html import mark_safe
from django.templatetags.static import static
from mptt.admin import DraggableMPTTAdmin
from adminsortable2.admin import SortableAdminMixin

from .models import *


admin.site.site_header = "Dandeline dashboard"
admin.site.site_title = "Dandeline dashboard"


admin.site.register(
    Category,
    DraggableMPTTAdmin,
    list_display=(
        "tree_actions",
        "indented_title",
    ),
    list_display_links=(
        "indented_title",
    ),
    prepopulated_fields={
        "slug": ("name",),
    },
)


class ProductImageInline(admin.TabularInline):
    model: type[Model] = ProductImage
    extra: int = 1


class VariationInline(admin.TabularInline):
    model: type[Model] = Variation
    extra: int = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display: Sequence[str] = ("preview", "name", "price", "active", "created_at")
    list_filter: Sequence[str] = ("created_at", "updated_at")
    list_editable: Sequence[str] = ("price", "active")
    prepopulated_fields: dict[str, Sequence[str]] = {
        "slug": ("name",),
    }
    readonly_fields: Sequence[str] = ("preview",)
    inlines: Sequence[type[InlineModelAdmin]] = (ProductImageInline, VariationInline)

    def preview(self, obj: Product) -> str:
        image_url: str = static("images/product-preview/placeholder.png")

        if obj.thumbnail:
            image_url = obj.thumbnail.url

        return mark_safe(f'<img src="{image_url}" width="85">')


@admin.register(Size)
class SizeAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display: Sequence[str] = ("order", "value")
