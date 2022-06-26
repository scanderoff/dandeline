from typing import Sequence
from decimal import Decimal

from django.conf import settings
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
# from django.utils.translation import gettext as _

from catalog.models import Variation
from coupons.models import Coupon


class Order(models.Model):
    class Meta:
        ordering: Sequence[str] = ("-created_at",)

    class ShippingMethod(models.TextChoices):
        POST: tuple[str, str] = ("post", "Доставка почтой")
        PICKPOINT: tuple[str, str] = ("pickpoint", "Постаматы PickPoint")
        ISSUEPOINT: tuple[str, str] = ("issuepoint", "Пункт выдачи в Иркутске")
        COURIER: tuple[str, str] = ("courier", "Курьерская доставка по Иркутску")

    class PaymentMethod(models.TextChoices):
        ONLINE: tuple[str, str] = ("online", "Онлайн")
        CASH: tuple[str, str] = ("cash", "Наличный расчёт")
        NONCASH: tuple[str, str] = ("noncash", "Безналичный расчёт")
        INSTALLMENT: tuple[str, str] = ("installment", "Рассрочка")
        COD: tuple[str, str] = ("cod", "Наложенный платеж")

    # class InstallmentPeriod(models.TextChoices):
    #     M6: tuple[str, str] = ("m6", "6 мес.")
    #     M10: tuple[str, str] = ("m10", "10 мес.")
    #     M12: tuple[str, str] = ("m12", "12 мес.")


    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="orders")
    coupon = models.ForeignKey(Coupon, related_name="orders", null=True, blank=True, on_delete=models.SET_NULL)
    discount = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])
    transaction_id = models.CharField(max_length=150, blank=True)

    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=50)
    email = models.EmailField(max_length=100, null=True, blank=True)
    zip_code = models.CharField(max_length=50)
    city = models.CharField(max_length=100)
    address1 = models.CharField(max_length=100)
    address2 = models.CharField(max_length=100, null=True, blank=True)
    shipping_method = models.CharField(max_length=20, default=ShippingMethod.POST, choices=ShippingMethod.choices)
    payment_method = models.CharField(max_length=20, default=PaymentMethod.ONLINE, choices=PaymentMethod.choices)
    note = models.TextField(max_length=300, null=True, blank=True)
    # installment_period = models.CharField(max_length=15, default=InstallmentPeriod.M6, choices=InstallmentPeriod.choices)

    paid = models.BooleanField(default=False)
    paid_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def total_price(self) -> Decimal:
        total_price: Decimal = sum(item.total_price for item in self.items.select_related("variation").all())
        return total_price - self.discount/Decimal(100) * total_price

    def __str__(self) -> str:
        return f"Order #{self.id}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    variation = models.ForeignKey(Variation, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    @property
    def total_price(self) -> Decimal:
        return self.quantity * self.variation.product.price

    def __str__(self) -> str:
        return f"{self.variation.product.name} ({self.quantity})"
