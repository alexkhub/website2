from django.core.files import File
from PIL import Image, ImageDraw
from io import BytesIO


def make_thumbnail(image, size=(200, 200)):
    """Создает миниатюры заданного размера"""
    im = Image.open(image)
    im.convert('RGB')
    im.thumbnail(size)
    thumb_io = BytesIO()
    mask = Image.new('L', im.size, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, im.width, im.height), fill=255)
    im.save(thumb_io, 'PNG', quality=85)
    thumbnail = File(thumb_io, name=image.name)
    return thumbnail
