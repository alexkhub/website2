from django.core.mail import send_mail

def send(mail_text, user_email):
    send_mail(
        'Добро пожаловать',
        mail_text,
        'aleksandrkhubaevwork@gmail.com',
        [user_email],
        fail_silently=False

    )