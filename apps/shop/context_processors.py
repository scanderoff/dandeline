from typing import Any

from django.http import HttpRequest

from .models import Category


def categories(request: HttpRequest) -> dict[str, Any]:
    return {
        "categories": Category.objects.all(),
        # .prefetch_related("children"),
    }
