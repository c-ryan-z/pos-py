from PyQt6.QtWidgets import QMessageBox
import random, uuid


# ------------------------WIDGETS:


def confirmAction(parent, title, subtitle, message):
    msg_box = QMessageBox(parent)
    msg_box.setWindowTitle(title)
    msg_box.setText(subtitle)
    msg_box.setInformativeText(message)
    msg_box.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
    msg_box.setDefaultButton(QMessageBox.StandardButton.No)
    reply = msg_box.exec()

    return reply == QMessageBox.StandardButton.Yes


# ------------------------- FUNCTIONS

def generate_code():
    code = random.randint(100000, 999999)
    # For this purpose, I'll use this RNG from Python, but in a real-world case, I'd use something secure.
    return f"{code:06d}"


def generate_session_id():
    return uuid.uuid4()
