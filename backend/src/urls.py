"""dandeline URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import URLPattern, path, include
from django.conf.urls.static import static


urlpatterns: list[URLPattern] = [
    path("admin/", admin.site.urls),

    path("my-account/", include("src.users.urls", namespace="users")),
    path("coupons/", include("src.coupons.urls", namespace="coupons")),
    path("payment/", include("src.payment.urls", namespace="payment")),
    path("orders/", include("src.orders.urls", namespace="orders")),
    path("cart/", include("src.cart.urls", namespace="cart")),
    path("bookmark/", include("src.bookmark.urls", namespace="bookmark")),
    path("catalog/", include("src.catalog.urls", namespace="catalog")),
    path("", include("src.marketing.urls", namespace="marketing")),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
