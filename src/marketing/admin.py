from typing import Sequence

from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin

from .models import HeroSlide


@admin.register(HeroSlide)
class HeroSlideAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display: Sequence[str] = ("image",)
