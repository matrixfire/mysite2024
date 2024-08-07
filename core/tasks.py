from celery import shared_task
from django.core.mail import send_mail



@shared_task
def test(name):
    """
    Task to send an e-mail notification when an order is
    successfully created.
    """

    subject = f'Order nr. {name}'
    message = (
        f'Dear fucking---{name},\n\n'
        f'You have successfully placed an order.'
        f'Your order ID is {name}.'
    )
    mail_sent = send_mail(
        subject, message, 'amazingtransition1@qq.com', ["matrixbox@qq.com"]
    )
    return mail_sent


@shared_task
def fucking_print(name):
    print("Fucking insane! ", name)
