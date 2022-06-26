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
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),

    path("my-account/", include("users.urls", namespace="users")),
    path("coupons/", include("coupons.urls", namespace="coupons")),
    path("payment/", include("payment.urls", namespace="payment")),
    path("orders/", include("orders.urls", namespace="orders")),
    path("cart/", include("cart.urls", namespace="cart")),
    path("bookmark/", include("bookmark.urls", namespace="bookmark")),
    path("catalog/", include("catalog.urls", namespace="catalog")),
    path("", include("marketing.urls", namespace="marketing")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
