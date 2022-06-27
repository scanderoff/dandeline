from typing import Sequence

from django.db import models


class HeroSlide(models.Model):
    image = models.ImageField(upload_to="hero_slide/%Y/%m/%d/")
    order = models.PositiveSmallIntegerField(default=0, db_index=True)
    link = models.CharField(max_length=200)

    class Meta:
        ordering: Sequence[str] = ("order",)


class Contact(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=60)
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.name} ({self.phone})"
