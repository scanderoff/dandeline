from celery import shared_task

from django.db.models import Model
from django.core.mail import send_mail
from django.contrib.auth import get_user_model

from .models import Order


User: type[Model] = get_user_model()


@shared_task
def order_created(order_id: int) -> int:
    order: Order = Order.objects.get(id=order_id)
    user: User = order.user

    subject = f"Интернет-магазин Dandeline"
    message = (
        f"Здравствуйте, {order.first_name},\n\n"

        f"Заказ №{order.id} принят.\n"
        f"Ваши данные для входа в личный кабинет:\n"
        f"Логин: {user.email}\n"
        f"Пароль: {user.password}\n"
    )

    mail_sent: int = send_mail(subject, message, "admin@dandeline.com", [order.email])

    return mail_sent
