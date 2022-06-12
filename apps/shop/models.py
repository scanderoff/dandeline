# from decimal import Decimal
from typing import Sequence
from django.shortcuts import reverse
from django.db import models
# from django.core.validators import MinValueValidator, MaxValueValidator
from django.templatetags.static import static
from mptt.models import MPTTModel, TreeForeignKey
from mptt.querysets import TreeQuerySet


class Category(MPTTModel):
    name = models.CharField(max_length=50)
    slug = models.SlugField(allow_unicode=True, unique=True, db_index=True)
    parent = TreeForeignKey(
        "self",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="children"
    )

    class Meta:
        verbose_name_plural: str = "categories"

    class MPTTMeta:
        order_insertion_by: list[str] = ["name"]

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self) -> str:
        tree: TreeQuerySet = self.get_ancestors(include_self=True)
        path: str = "/".join(node.slug for node in tree)

        return reverse("shop:catalog", kwargs={
            "path": path,
        })


class Product(models.Model):
    sku = models.CharField(max_length=15, unique=True, blank=True)
    category = TreeForeignKey(Category, on_delete=models.PROTECT)
    name = models.CharField(max_length=150)
    slug = models.SlugField(allow_unicode=True, unique=True, db_index=True)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    active = models.BooleanField(default=True)
    thumbnail = models.ImageField(upload_to="product/%Y/%m/%d/", null=True, blank=True)
    # discount = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # @property
    # def discounted_price(self) -> Decimal:
    #     return self.price  - (self.price * self.discount)

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self) -> str:
        return reverse("shop:product", kwargs={
            "slug": self.slug,
        })

    @property
    def thumbnail_url(self) -> str:
        url: str = static("images/product-preview/placeholder.png")

        if self.thumbnail:
            url = self.thumbnail.url

        return url


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="images")
    file = models.ImageField(upload_to="product_image/%Y/%m/%d/")


class Size(models.Model):
    value = models.CharField(max_length=20)
    order = models.PositiveSmallIntegerField(default=0, db_index=True)

    class Meta:
        ordering: Sequence[str] = ("order",)

    def __str__(self) -> str:
        return self.value


class Variation(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="variations")
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    # other attributes, e.g. color

    def __str__(self) -> str:
        return f"{self.product} (size: {self.size})"
