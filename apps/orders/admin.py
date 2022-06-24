import csv
import datetime

from typing import Any, Callable

from django.contrib import admin
from django.http import HttpRequest, HttpResponse
from django.db.models import QuerySet
from django.urls import reverse
from django.utils.html import mark_safe

from .models import *


def export_to_csv(modeladmin: admin.ModelAdmin, request: HttpRequest, queryset: QuerySet) -> HttpResponse:
    opts = modeladmin.model._meta
    content_disposition: str = f"attachment; filename={opts.verbose_name}.csv"
    response: HttpResponse = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = content_disposition
    writer = csv.writer(response)

    fields = [field for field in opts.get_fields() if not field.many_to_many and not field.one_to_many]

    writer.writerow([field.verbose_name for field in fields])

    for obj in queryset:
        data_row: list[str] = []

        for field in fields:
            value: Any = getattr(obj, field.name)

            if isinstance(value, datetime.datetime):
                value: str = value.strftime("%d/%m/%Y")

            data_row.append(value)

        writer.writerow(data_row)

    return response

export_to_csv.short_description = "Export to CSV"


def order_pdf(obj: Order) -> str:
    url: str = reverse("orders:admin_order_pdf", kwargs={
        "order_id": obj.id,
    })

    return mark_safe(f'<a href="{url}">PDF</a>')

order_pdf.short_description = "Invoice"


class OrderItemInline(admin.TabularInline):
    model: type = OrderItem
    raw_id_fields: list[str] = ("variation",)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display: list[str] = ["id", "user", "paid", order_pdf]
    list_filter: list[str] = ["paid", "created_at"]
    inlines: list[type] = [OrderItemInline,]
    actions: Callable[..., HttpResponse] = [export_to_csv]
