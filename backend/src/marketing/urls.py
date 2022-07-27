from django.urls import URLPattern, path

from .apps import MarketingConfig
from . import views


app_name: str = MarketingConfig.name

urlpatterns: list[URLPattern] = [
    path("", views.homepage, name="homepage"),
    path("delivery-and-payment/", views.delivery_and_payment, name="delivery-and-payment"),
    path("return/", views.return_, name="return"),
    path("about-us/", views.about_us, name="about-us"),
    path("contact/", views.contact, name="contact"),

    path("leave-contact/", views.leave_contact, name="leave-contact"),

    path("hero-slides/", views.HeroSlideListAPIView.as_view(), name="hero-slides"),
    path("contact-create/", views.ContactCreateAPIView.as_view(), name="contact-create"),
]
