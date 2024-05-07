import io
import random
import uuid
from typing import Union

from PIL import Image, ImageDraw, ImageQt
from PyQt6.QtGui import QColor, QPixmap, QImage
from PyQt6.QtWidgets import QGraphicsDropShadowEffect


# ------------------------WIDGETS:

def shadow_effect(widget):
    shadow = QGraphicsDropShadowEffect()
    shadow.setBlurRadius(20)
    shadow.setXOffset(0)
    shadow.setYOffset(0)
    shadow.setColor(QColor(0, 0, 0, 80))
    widget.setGraphicsEffect(shadow)


def img_radius(ipt: Union[str, bytes], radius: int):
    if isinstance(ipt, str):
        image = Image.open(ipt)
    else:
        image = Image.open(io.BytesIO(ipt))

    circle = Image.new('L', (radius * 2, radius * 2), 0)
    draw = ImageDraw.Draw(circle)
    draw.ellipse((0, 0, radius * 2, radius * 2), fill=255)

    alpha = Image.new('L', image.size, 255)
    w, h = image.size
    alpha.paste(circle.crop((0, 0, radius, radius)), (0, 0))
    alpha.paste(circle.crop((0, radius, radius, radius * 2)), (0, h - radius))
    alpha.paste(circle.crop((radius, 0, radius * 2, radius)), (w - radius, 0))
    alpha.paste(circle.crop((radius, radius, radius * 2, radius * 2)), (w - radius, h - radius))

    image.putalpha(alpha)

    qim = ImageQt.ImageQt(image)
    qImage = QImage(qim)
    pixmap = QPixmap.fromImage(qImage)
    return pixmap


# ------------------------- FUNCTIONS

def generate_code():
    code = random.randint(100000, 999999)
    # For this purpose, I'll use this RNG from Python, but in a real-world case, I'd use something secure.
    return f"{code:06d}"


def generate_session_id():
    return uuid.uuid4()


def process_data(tbl_data, col):
    processed_data = []
    for row in tbl_data:
        row = list(row)
        row[col] = "Done" if row[col] else "Voided"
        row.append("Detail")
        processed_data.append(tuple(row))
    return processed_data
