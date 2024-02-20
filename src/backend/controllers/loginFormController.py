from PyQt6 import QtWidgets as Qtw
from PyQt6 import QtCore

import hashlib

from src.frontend.loginFormUi import Ui_Form
from src.backend.database import loginUser


class LoginForm(Qtw.QWidget):
    userLoggedIn = QtCore.pyqtSignal(tuple)

    def __init__(self, main_app):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.main_app = main_app

        self.ui.pb_logIn.clicked.connect(self.handleLogin)

    def handleLogin(self):
        username = self.ui.le_username.text()
        password = self.ui.le_pass.text()
        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        user = loginUser(username, hashed_password)
        if user is not None:
            self.ui.le_username.clear()
            self.ui.le_pass.clear()

            self.userLoggedIn.emit(user)
        else:
            print("Login Failed")
