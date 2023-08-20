from celery import shared_task
from django.core.mail import send_mail
from . models import Order

@shared_task
def order_created(order_id):

        """ Task to send an email when order is successfully created"""
        order = Order.objects.get(id=order_id)
        subject = f'Order no: {order.id}'
        message = f'Dear {order.first_name}, \n\n' \
                f'You have successfuly placed an order' \
                f'Your order is: {order.id}'
        mail_sent = send_mail(subject, message, 'procentstore@gmail.com', [order.email])
        return mail_sent