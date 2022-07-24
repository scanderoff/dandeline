from typing import Any

from django.apps import apps
from django.db import models
from django.db.models import QuerySet, Prefetch


class ProductManager(models.Manager):
    """Custom product manager"""

    def get_queryset(self) -> QuerySet:
        Variation = apps.get_model("catalog", "Variation")

        return (super().get_queryset()
            .prefetch_related(Prefetch(
                "variations",
                queryset=Variation.objects
                    .select_related("size")
                    .order_by("size__value")
                ,
                to_attr="sizes",
            ))
            .prefetch_related(Prefetch(
                "variations",
                queryset=Variation.objects
                    .select_related("color")
                    .order_by("color__value")
                ,
                to_attr="colors",
            ))
        )
