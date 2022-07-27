import json

from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render
from django.db.models import QuerySet
from django.views.decorators.http import require_POST
from rest_framework.generics import ListAPIView, CreateAPIView

from src.catalog.models import Category, Product
from src.bookmark.services.bookmark import Bookmark
from .models import HeroSlide, Contact
from .forms import ContactForm
from .serializers import HeroSlideSerializer, ContactSerializer


class HeroSlideListAPIView(ListAPIView):
    queryset = HeroSlide.objects.all()
    serializer_class = HeroSlideSerializer


class ContactCreateAPIView(CreateAPIView):
    model = Contact
    serializer_class = ContactSerializer


def homepage(request: HttpRequest) -> HttpResponse:
    hero_slides: QuerySet[HeroSlide] = HeroSlide.objects.all()
    featured_cats: QuerySet[Category] = Category.objects.filter(featured=True)
    new_products: QuerySet[Product] = Product.objects.order_by("-created_at")[:8]
    popular_products: QuerySet[Product] = Product.objects.order_by("-total_sales")[:4]

    # return HttpResponse("111")
    return render(request, "marketing/homepage.html", {
        "hero_slides": hero_slides,
        "featured_cats": featured_cats,
        "new_products": new_products,
        "popular_products": popular_products,
        "bookmark": Bookmark(request),
    })


def contact(request: HttpRequest) -> HttpResponse:
    return render(request, "marketing/contact.html", {})


def about_us(request: HttpRequest) -> HttpResponse:
    return render(request, "marketing/about_us.html", {})


def return_(request: HttpRequest) -> HttpResponse:
    return render(request, "marketing/return.html", {})


def delivery_and_payment(request: HttpRequest) -> HttpResponse:
    return render(request, "marketing/delivery_and_payment.html", {})


@require_POST
def leave_contact(request: HttpRequest) -> HttpResponse:
    data = json.loads(request.body)
    form = ContactForm(data)

    if not form.is_valid():
        return JsonResponse({"success": False})

    form.save()

    return JsonResponse({
        "success": True,
    })
