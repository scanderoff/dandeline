from tabnanny import verbose
from typing import Sequence

from django.db import models


class HeroSlide(models.Model):
    class Meta:
        ordering: Sequence[str] = ("order",)
        verbose_name = 'Hero слайд'
        verbose_name_plural = 'Hero слайды'


    image = models.ImageField(upload_to="hero_slide/%Y/%m/%d/")
    order = models.PositiveSmallIntegerField(default=0, db_index=True)
    link = models.CharField(max_length=200)


class Contact(models.Model):
    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'


    name = models.CharField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=60)
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.name} ({self.phone})"
