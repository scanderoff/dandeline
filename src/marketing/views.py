from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.db.models import QuerySet

from catalog.models import Category, Product
from .models import HeroSlide


def homepage(request: HttpRequest) -> HttpResponse:
    hero_slides: QuerySet[HeroSlide] = HeroSlide.objects.all()
    featured_cats: QuerySet[Category] = Category.objects.filter(featured=True)
    new_products: QuerySet[Product] = Product.objects.order_by("-created_at")[:8]
    popular_products: QuerySet[Product] = Product.objects.order_by("-total_sales")[:4]

    return render(request, "marketing/homepage.html", {
        "hero_slides": hero_slides,
        "featured_cats": featured_cats,
        "new_products": new_products,
        "popular_products": popular_products,
    })
