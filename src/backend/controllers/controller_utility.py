import random
import uuid

from PyQt6.QtGui import QColor
from PyQt6.QtWidgets import QGraphicsDropShadowEffect


# ------------------------WIDGETS:

def shadow_effect(widget):
    shadow = QGraphicsDropShadowEffect()
    shadow.setBlurRadius(20)
    shadow.setXOffset(0)
    shadow.setYOffset(0)
    shadow.setColor(QColor(0, 0, 0, 80))
    widget.setGraphicsEffect(shadow)


# ------------------------- FUNCTIONS

def generate_code():
    code = random.randint(100000, 999999)
    # For this purpose, I'll use this RNG from Python, but in a real-world case, I'd use something secure.
    return f"{code:06d}"


def generate_session_id():
    return uuid.uuid4()
