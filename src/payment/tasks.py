import weasyprint

from io import BytesIO
from celery import shared_task

from django.conf import settings
from django.template.loader import render_to_string
from django.core.mail import EmailMessage

from orders.models import Order


@shared_task
def payment_completed(order_id: int) -> None:
    order: Order = Order.objects.get(id=order_id)

    subject: str = f"Dandeline - Счет №{order.id}"
    message: str = "Пожалуйста, проверьте прикрепленный счет последней покупки."

    email = EmailMessage(subject, message, "admin@dandeline.com", [order.email])

    html: str = render_to_string("orders/pdf.html", {"order": order})
    out = BytesIO()
    stylesheets = [weasyprint.CSS(settings.STATIC_ROOT / "styles/pdf.css")]
    weasyprint.HTML(string=html).write_pdf(out, stylesheets=stylesheets)

    email.attach(f"order_{order.id}.pdf", out.getvalue(), "application/pdf")
    email.send()
