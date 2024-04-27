import sys
import time

from PyQt6 import QtWidgets as Qtw, QtCore
from dotenv import load_dotenv
from pyqt6_plugins.examplebuttonplugin import QtGui

from src.backend.controllers.__customWidget.userInfoController import UserInfoWidget
from src.backend.controllers.adminControllers.adminController import AdminController
from src.backend.controllers.loginControllers.loginFormController import LoginForm
from src.backend.controllers.loginControllers.otpController import OTPForm
from src.backend.controllers.loginControllers.pw_resetController import PasswordReset
from src.backend.controllers.salesControllers.SalesController import SalesController
from src.setup_paths import Paths


class MainApp(Qtw.QWidget):
    mainLoggedIn = QtCore.pyqtSignal(tuple)

    def __init__(self):
        super().__init__()
        # todo handle the printing and add a loading to all instances
        self.userInfo = None
        self.setMinimumSize(1920, 1040)
        self.setWindowTitle("Point Of Sales")
        self.setWindowIcon(QtGui.QIcon(Paths.image("logo_u2.png")))

        self.userInfoController = UserInfoWidget(self)

        self.stacked_widget = Qtw.QStackedWidget()
        self.stacked_widget.setSizePolicy(Qtw.QSizePolicy.Policy.Expanding, Qtw.QSizePolicy.Policy.Expanding)
        self.stacked_widget.setStyleSheet("font-family: 'Inter';")
        self.widgets = {}

        self.login_form = LoginForm(self)
        self.addWidget(self.login_form, 'login')

        self.password_reset = PasswordReset(self)
        self.addWidget(self.password_reset, 'password_reset')

        self.otpController = OTPForm(self, self.login_form)
        self.addWidget(self.otpController, 'otp')

        self.admin = AdminController()
        self.addWidget(self.admin, 'admin')

        self.salesController = SalesController(self, self.userInfoController)
        self.addWidget(self.salesController, 'cashier')

        self.darkener = Qtw.QWidget(self.stacked_widget)
        self.darkener.setGeometry(self.rect())
        self.darkener.setStyleSheet("background-color: rgba(180,180,180,0.78);")
        self.darkener.hide()

        self.layout = Qtw.QVBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.addWidget(self.stacked_widget)

        self.darkener.raise_()

        self.setLayout(self.layout)

        self.key_sequence = ""
        self.last_key_time = time.time()

    def addWidget(self, widget, identifier):
        self.widgets[identifier] = self.stacked_widget.addWidget(widget)

    def setCurrentWidget(self, identifier):
        if identifier in self.widgets:
            self.stacked_widget.setCurrentIndex(self.widgets[identifier])

    def showDarkener(self):
        self.darkener.show()
        self.darkener.raise_()

    def hideDarkener(self):
        self.darkener.hide()

    def closeEvent(self, event):
        if self.userInfoController is not None and self.userInfoController.user_info is not None:
            if not self.userInfoController.handleLogout():
                event.ignore()
                return
        super().closeEvent(event)


if __name__ == '__main__':
    app = Qtw.QApplication(sys.argv)
    main_app = MainApp()
    load_dotenv()
    main_app.showMaximized()
    sys.exit(app.exec())
