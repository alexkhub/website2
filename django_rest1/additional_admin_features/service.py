from django.core.mail import send_mail
from datetime import date , timedelta


def send(mail_text, user_email):
    send_mail(
        'Добро пожаловать',
        mail_text,
        'aleksandrkhubaevwork@gmail.com',
        [user_email],
        fail_silently=False

    )

def yesterday():
    day = date.today()
    yesterday = day - timedelta(days=1)
    return yesterday




#Users.objects.filter(last_login__contains =day ))