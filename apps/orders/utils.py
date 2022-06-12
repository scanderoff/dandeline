from users.models import User
from orders.models import Order
from .models import Order


def register_on_checkout(order: Order) -> User:
    password: str = User.objects.make_random_password()

    user: User = User.objects.create(
        email=order.email,
        password=password,

        first_name=order.first_name,
        last_name=order.last_name,
        phone=order.phone,
        zip_code=order.zip_code,
        city=order.city,
        address_1=order.address_1,
        address_2=order.address_2,
    )

    return user
