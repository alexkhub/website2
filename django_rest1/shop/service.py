from django.core.mail import send_mail

from datetime import date , timedelta


def send(user_email):
    send_mail(
        'Добро пожаловать',
        'Мы будем присылать вам QR код ',
        'aleksandrkhubaevwork@gmail.com',
        [user_email],
        fail_silently=False

    )
def yesterday():
    day = date.today()
    yesterday = day - timedelta(days=1)
    return yesterday