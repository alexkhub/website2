from django.core.mail import send_mail
from datetime import date, timedelta
from PIL import Image, ImageDraw


def update_photo(img):
    size = (200, 200)
    original = Image.open(img)
    original.thumbnail(size)
    mask = Image.new('L', original.size, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, original.width, original.height), fill=255)
    result = Image.new('RGBA', original.size)
    result.paste(original, (0, 0), mask=mask)
    return result

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
