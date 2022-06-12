import redis

from django.conf import settings

from .models import Product


r = redis.Redis(
    host=settings.REDIS_HOST,
    port=settings.REDIS_PORT,
    db=settings.REDIS_DB
)


class Recommender:
    def get_product_key(self, id: int) -> str:
        return f"product:{id}:purchased_with"

    def products_bought(self, products: list[Product]) -> None:
        """
        Итерируемся по идам продуктов и для каждого продукта в его сете
        инкрементируем число покупок других продуктов в том же списке
        """

        product_ids = [product.id for product in products]

        for product_id in product_ids:
            for with_id in product_ids:
                if product_id != with_id:
                    r.zincrby(self.get_product_key(product_id), 1, with_id)

    def suggest_products_for(self, products: list[Product], max_results: int = 6) -> list[Product]:
        product_ids: list[int] = [product.id for product in products]

        if len(products) == 1:
            suggestions = r.zrange(self.get_product_key(product_ids[0]),
                                   0, max_results - 1, desc=True)
        else:
            flat_ids: str = "".join([str(id) for id in product_ids])
            tmp_key: str = f"tmp_{flat_ids}"
            keys: list[str] = [self.get_product_key(id) for id in product_ids]

            r.zunionstore(tmp_key, keys)

            r.zrem(tmp_key, *product_ids)

            suggestions: list[bytes] = r.zrange(tmp_key, 0, max_results - 1, desc=True)

            r.delete(tmp_key)

        suggested_products_ids = [int(id) for id in suggestions]
        suggested_products = list(Product.objects.filter(id__in=suggested_products_ids))
        suggested_products.sort(key=lambda x: suggested_products_ids.index(x.id))

        return suggested_products

    def clear_purchases(self) -> None:
        for id in Product.objects.values_list("id", flat=True):
            r.delete(self.get_product_key(id))
