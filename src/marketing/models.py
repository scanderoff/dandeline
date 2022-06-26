from typing import Sequence

from django.db import models


class HeroSlide(models.Model):
    image = models.ImageField(upload_to="hero_slide/%Y/%m/%d/")
    order = models.PositiveSmallIntegerField(default=0, db_index=True)
    link = models.URLField()

    class Meta:
        ordering: Sequence[str] = ("order",)
