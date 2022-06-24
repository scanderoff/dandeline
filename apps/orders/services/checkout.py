from django.http import HttpRequest
from django.db.models import Model
from django.forms import ValidationError
from django.contrib.auth import get_user_model, login

from cart.services.cart import Cart
from ..models import Order, OrderItem
from ..forms import OrderCreateForm
from ..tasks import order_created


User: type[Model] = get_user_model()






def register_on_checkout(request: HttpRequest, order: Order) -> User:
    """Register after placing order"""
    password: str = User.objects.make_random_password()

    user: User = User.objects.from_order(order, password)
    login(request, user)

    return user



class CheckoutProcessor:
    """Processes checkout"""

    def __init__(self, request: HttpRequest) -> None:
        self.request = request
        self.cart = Cart(request)
        self.form = OrderCreateForm(request.POST)
        self.order = None

    def run(self) -> None:
        self.__create_order()

        self.__create_order_items()

        order_created.delay(self.order.id)

        self.request.session["order_id"] = self.order.id

    def __create_order(self) -> None:
        if not self.form.is_valid():
            raise ValidationError()

        self.order = self.form.save(commit=False)
        user: User = self.request.user

        if not user.is_authenticated:
            user = register_on_checkout(self.request, self.order)

        self.order.user = user

        if self.cart.coupon:
            self.order.coupon = self.cart.coupon
            self.order.discount = self.cart.coupon.discount

        self.order.save()

    def __create_order_items(self) -> None:
        order_items: list[OrderItem] = []

        for item in self.cart:
            order_item = OrderItem(
                order=self.order,
                variation=item["variation"],
                quantity=item["quantity"],
            )

            order_items.append(order_item)

        OrderItem.objects.bulk_create(order_items)

        self.cart.clear()
