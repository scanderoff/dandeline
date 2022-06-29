from typing import Sequence
from django.shortcuts import reverse
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from mptt.querysets import TreeQuerySet

from .managers import ProductManager


class Category(MPTTModel):
    """Product category"""

    class Meta:
        verbose_name_plural = "categories"
        unique_together = ("slug", "parent")
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    class MPTTMeta:
        order_insertion_by: list[str] = ["name"]

    name = models.CharField(max_length=50)
    slug = models.SlugField(allow_unicode=True, db_index=True)
    parent = TreeForeignKey(
        "self",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="children"
    )
    image = models.ImageField(
        upload_to="category",
        default="placeholder.png",
        null=True,
        blank=True
    )
    featured = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self) -> str:
        tree: TreeQuerySet = self.get_ancestors(include_self=True)
        path: str = "/".join(node.slug for node in tree)

        return reverse("catalog:products", kwargs={
            "path": path,
        })


class Product(models.Model):
    """Represents a product"""

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    sku = models.CharField(max_length=15, unique=True, blank=True)
    category = TreeForeignKey(Category, on_delete=models.PROTECT)
    name = models.CharField(max_length=150)
    slug = models.SlugField(allow_unicode=True, unique=True, db_index=True)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    active = models.BooleanField(default=True)
    thumbnail = models.ImageField(
        upload_to="product/%Y/%m/%d/",
        default="placeholder.png",
        null=True,
        blank=True,
    )
    total_sales = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = ProductManager()


    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self) -> str:
        return reverse("catalog:product", kwargs={
            "slug": self.slug,
        })



class ProductImage(models.Model):
    """Each product has a set of images on their detail page"""

    class Meta:
        verbose_name = 'Изображение продукта'
        verbose_name_plural = 'Изображения продукта'

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="images")
    file = models.ImageField(upload_to="product_image/%Y/%m/%d/")


class Size(models.Model):
    """Product size attribute"""

    class Meta:
        ordering: Sequence[str] = ("order",)
        verbose_name = 'Размер'
        verbose_name_plural = 'Размеры'

    value = models.CharField(max_length=20)
    order = models.PositiveSmallIntegerField(default=0, db_index=True)

    def __str__(self) -> str:
        return self.value


class Color(models.Model):
    """Product color attribute"""

    class Meta:
        verbose_name = 'Цвет'
        verbose_name_plural = 'Цвета'

    value = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.value


class Variation(models.Model):
    """Intermediary model for product variations"""

    class Meta:
        verbose_name = 'Вариация'
        verbose_name_plural = 'Вариации'

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="variations")
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    # other attributes

    def __str__(self) -> str:
        return f"{self.product} (size: {self.size}, color: {self.color})"
