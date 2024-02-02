from PyQt6 import QtWidgets as qtw

from src.frontend.loginFormUi import Ui_Form
from src.backend.database import loginUser

class LoginForm(qtw.QWidget):
    def __init__(self, main_app):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.main_app = main_app

        self.ui.pb_logIn.clicked.connect(self.handleLogin)


    def handleLogin(self):
        username = self.ui.le_username.text()
        password = self.ui.le_pass.text()

        user = loginUser(username, password)
        if user is not None:
            user_role = user[2]
            self.main_app.setCurrentWidget(user_role)
        else:
            print("Login Failed")
