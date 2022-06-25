from typing import Any

from django.apps import apps
from django.db import models
from django.db.models import Prefetch


class ProductManager(models.Manager):
    """Custom product manager"""

    def prefetch_attributes(self) -> models.QuerySet:
        """Предварительно запрашиваем вариации"""

        Variation = apps.get_model("shop", "Variation")

        return (self
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
