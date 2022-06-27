from typing import Any

from django.http import HttpRequest

from .forms import ContactForm


def contact_form(_: HttpRequest) -> dict[str, Any]:
    contact_form = ContactForm(auto_id=False)

    return {
        "contact_form": contact_form,
    }
