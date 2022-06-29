import json
import random
import faker
import faker.providers
from typing import Any

from django.core.management.base import BaseCommand

from catalog.models import Product, Variation, Size, Color


class Command(BaseCommand):
    help = "Command info"

    def handle(self, *args: Any, **kwargs: dict[str, Any]) -> None:
        fake = faker.Faker(["ru_RU"])

        with open("src/catalog/fixtures/categories.json", "r") as inf:
            categories: dict[str, Any] = json.loads(inf.read())

        print(categories)
        sizes: list[Size] = []

        for _ in range(15):
            sizes.append(Size(
                value=fake.unique.random_int(min=40, max=100, step=2),
            ))

        Size.objects.bulk_create(sizes)


        colors: list[Color] = []

        for _ in range(10):
            colors.append(Color(
                value=fake.unique.color(),
            ))

        Color.objects.bulk_create(colors)



        faker.Faker.seed(0)
        for _ in range(30):
            product = Product.objects.create(
                sku=fake.bothify(text="??????-########"),
                category_id=fake.random_element(elements=categories)["pk"],
                name=fake.unique.name(),
                slug=fake.unique.word(),
                description="\r\n".join(fake.paragraphs(nb=2)),
                price=round(random.uniform(930.00, 9700.00), 2),
            )

            for _ in range(random.randrange(3, 8)):
                Variation.objects.create(
                    product=product,
                    size=fake.random_element(elements=sizes),
                    color=fake.random_element(elements=colors),
                )
