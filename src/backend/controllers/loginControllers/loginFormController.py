from PyQt6 import QtWidgets as Qtw
from PyQt6 import QtCore

import hashlib

from PyQt6.QtCore import QPropertyAnimation, QPoint, QEasingCurve

from src.backend.database.record_logins import record_login_attempt
from src.frontend.loginForm import Ui_Form
from src.backend.database.auth import login_user, check_db_for_user, login_attempt, otp_attempts


class LoginForm(Qtw.QWidget):
    userLoggedIn = QtCore.pyqtSignal(tuple)

    def __init__(self, main_app):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.animation = None
        self.animation2 = None
        self.user = None
        self.main_app = main_app

        self.ui.le_username.installEventFilter(self)
        self.ui.le_pass.installEventFilter(self)
        self.ui.pb_logIn.installEventFilter(self)

        self.ui.pb_logIn.clicked.connect(self.handleLogin)

    def handleLogin(self):
        username = self.ui.le_username.text()
        password = self.ui.le_pass.text()
        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        user_exists = check_db_for_user(username)

        if user_exists is None:
            print("No user found")
            return

        user = login_user(username, hashed_password)
        wrong_attempts = login_attempt(user_exists[0])

        if wrong_attempts is not None and wrong_attempts[1] >= 3:
            print("Too many wrong attempts try again later")
            self.ui.le_pass.clear()
            return

        if user is None:
            record_login_attempt(user_exists[0], False, 'placeholder')
            print("Wrong password")
            self.ui.le_pass.clear()
            return

        otp_count = otp_attempts(user[0])

        if user[3] and otp_count is not None and otp_count >= 3:
            print("Too many OTP attempts")
            return

        record_login_attempt(user[0], True, 'placeholder')
        self.ui.le_username.clear()
        self.ui.le_pass.clear()
        self.ui.le_username.setFocus()
        self.user = user
        self.transitionGb()

    def eventFilter(self, obj, event):
        if event.type() == QtCore.QEvent.Type.KeyPress and event.key() == QtCore.Qt.Key.Key_Return:
            self.handleLogin()
            return True
        return super().eventFilter(obj, event)

    def transitionGb(self, reverse=False):
        end_val1 = QPoint(self.ui.gb_banner.pos().x() - self.ui.gb_banner.width(), self.ui.gb_banner.y())
        end_val2 = QPoint(self.ui.gb_login.pos().x() + self.ui.gb_login.width(), self.ui.gb_login.y())

        if reverse:
            end_val1 = QPoint(self.ui.gb_banner.pos().x() + self.ui.gb_banner.width(), self.ui.gb_banner.y())
            end_val2 = QPoint(self.ui.gb_login.pos().x() - self.ui.gb_login.width(), self.ui.gb_login.y())

        self.animation = QPropertyAnimation(self.ui.gb_banner, b"pos")
        self.animation.setStartValue(self.ui.gb_banner.pos())
        self.animation.setEndValue(end_val1)
        self.animation.setDuration(600)
        self.animation.setEasingCurve(QEasingCurve.Type.InOutCubic)

        self.animation2 = QPropertyAnimation(self.ui.gb_login, b"pos")
        self.animation2.setStartValue(self.ui.gb_login.pos())
        self.animation2.setEndValue(end_val2)
        self.animation2.setDuration(600)
        self.animation2.setEasingCurve(QEasingCurve.Type.InOutCubic)

        self.animation.start()
        self.animation2.start()

        self.animation.finished.connect(lambda: self.userLoggedIn.emit(self.user))
