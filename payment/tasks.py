from io import BytesIO

from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings

from celery import shared_task
import weasyprint

from orders.models import Order

@shared_task
def payment_completed(order_id):
    """ Task to send an email notification when an order is successfully created """
    order = Order.objects.get(id=order_id)

    # create invoice email 
    subject = f'procent store - EE Invoice no. {order.id}'
    message = 'please find attached the invoice for you recent purchase'
    email = EmailMessage(subject,message, 'procentstore@gmail.com', [order.email])

    # generate pdf 
    html =render_to_string('orders/order/pdf.html', {'order': order})
    out = BytesIO()
    stylesheets = [weasyprint.css(settings.STATIC_ROOT + 'css/pdf.css')]
    weasyprint.HTML(string=html).write_pdf(out, stylesheets=stylesheets)

    # attach pdf file to email 
    email.attach(f'order_{order.id}.pdf', out.getvalue(), 'application/pdf')
    # send email 
    email.send()