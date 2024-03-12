import sys

from PyQt6 import QtWidgets as Qtw
from PyQt6 import QtCore
from dotenv import load_dotenv

from src.backend.controllers.adminControllers.adminController import AdminController
from src.backend.controllers.__customWidget.userInfoController import UserInfoWidget
from src.backend.controllers.salesControllers.salesController import SalesController
from src.backend.controllers.loginControllers.otpController import OTPForm
from src.backend.controllers.loginControllers.loginFormController import LoginForm


class MainApp(Qtw.QWidget):
    mainLoggedIn = QtCore.pyqtSignal(tuple)

    def __init__(self):
        super().__init__()
        # todo handle the printing and add a loading to all instances
        self.userInfo = None
        self.setMinimumSize(1920, 1040)
        self.setWindowTitle("Point Of Sales")

        self.userInfoController = UserInfoWidget(self)

        self.stacked_widget = Qtw.QStackedWidget()
        self.stacked_widget.setStyleSheet("font-family: 'Inter';")
        self.widgets = {}

        self.login_form = LoginForm(self)
        self.login_form.userLoggedIn.connect(self.otp_verify)
        self.addWidget(self.login_form, 'login')

        self.otpController = OTPForm(self, self.login_form)
        self.otpController.OtpVerified.connect(self.setCurrentWidget)
        self.addWidget(self.otpController, 'otp')

        self.admin = AdminController()
        self.addWidget(self.admin, 'admin')

        self.salesController = SalesController(self, self.userInfoController)
        self.addWidget(self.salesController, 'cashier')

        layout = Qtw.QVBoxLayout()

        layout.addWidget(self.stacked_widget)

        self.setLayout(layout)

    def addWidget(self, widget, identifier):
        self.widgets[identifier] = self.stacked_widget.addWidget(widget)

    def setCurrentWidget(self, identifier):
        if identifier in self.widgets:
            self.stacked_widget.setCurrentIndex(self.widgets[identifier])

    def nextWidget(self):
        self.stacked_widget.setCurrentIndex((self.stacked_widget.currentIndex() + 1) % self.stacked_widget.count())

    def otp_verify(self, user_info):
        self.userInfo = user_info
        if user_info[3]:
            self.setCurrentWidget('otp')
            return

        self.setCurrentWidget(user_info[2])
        self.mainLoggedIn.emit(user_info)


if __name__ == '__main__':
    app = Qtw.QApplication(sys.argv)
    main_app = MainApp()
    load_dotenv()
    main_app.showMaximized()
    sys.exit(app.exec())
