from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from django.contrib import messages

from .bookmark import Bookmark


def summary(request: HttpRequest) -> HttpResponse:
    bookmark = Bookmark(request)

    if len(bookmark) == 0:
        messages.error(request, "У Вас пока нет избранных товаров.")

    return render(request, "bookmark/summary.html", {
        "bookmark": bookmark,
    })


@require_POST
def update(request: HttpRequest, product_id: int) -> HttpResponse:
    bookmark = Bookmark(request)

    action: str = request.POST["action"]

    if action == "add":
        bookmark.add(product_id)
    elif action == "remove":
        bookmark.remove(product_id)

    return redirect(request.META.get("HTTP_REFERER", "/"))


@require_POST
def clear(request: HttpRequest) -> HttpResponse:
    bookmark = Bookmark(request)
    bookmark.clear()

    return redirect(request.META.get("HTTP_REFERER", "/"))
