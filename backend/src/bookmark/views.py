from django.contrib import messages
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.views.decorators.http import require_POST
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import BookmarkSerializer
from .services.bookmark import Bookmark


class BookmarkAPIView(APIView):
    def get(self, request: Request) -> Response:
        bookmark = Bookmark(request)
        serializer = BookmarkSerializer(bookmark)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request: Request) -> Response:
        bookmark = Bookmark(request)

        product_id: str = request.data["product_id"]
        action: str = request.data["action"]

        if action == "add":
            bookmark.add(product_id)
        elif action == "remove":
            bookmark.remove(product_id)

        serializer = BookmarkSerializer(bookmark)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request: Request) -> Response:
        bookmark = Bookmark(request)
        bookmark.clear()

        return Response(status.HTTP_204_NO_CONTENT)


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
