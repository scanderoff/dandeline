from django.contrib import admin

from .models import Coupon


@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    list_display: list[str] = ["code", "valid_from", "valid_to", "discount", "active"]
    list_filter: list[str] = ["active", "valid_from", "valid_to"]
    search_fields: list[str] = ["code"]