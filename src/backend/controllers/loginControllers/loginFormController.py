from PyQt6 import QtWidgets as Qtw, QtCore

from src.backend.threads.login.login_thread import LoginThread
from src.backend.controllers.controller_utility import shadow_effect
from src.frontend.login.loginForm import Ui_login_form
from src.backend.controllers.__customWidget.CustomMessageBox import CustomMessageBox


class LoginForm(Qtw.QWidget):
    otp_signal = QtCore.pyqtSignal(tuple)

    def __init__(self, main_app):
        super().__init__()
        self.ui = Ui_login_form()
        self.ui.setupUi(self)
        self.user = None
        self.login_id = None
        self.main_app = main_app
        self.login_thread = LoginThread(self)

        self.login_thread.finished.connect(self.on_handle_login_finished)
        self.login_thread.otp_signal.connect(self.handle_otp_signal)
        self.login_thread.error_signal.connect(self.handle_error_signal)

        self.ui.le_username.installEventFilter(self)
        self.ui.le_pass.installEventFilter(self)
        self.ui.pb_logIn.installEventFilter(self)
        self.ui.le_status.setVisible(False)

        self.ui.pb_logIn.clicked.connect(self.startLoginThread)
        self.ui.pb_forgotpw.clicked.connect(lambda: self.main_app.setCurrentWidget('password_reset'))
        self.ui.checkBox.stateChanged.connect(self.custom_box)

        shadow_effect(self.ui.lb_sys)
        shadow_effect(self.ui.gb_form)

    def startLoginThread(self):
        if self.ui.pb_logIn.isEnabled():
            self.ui.pb_logIn.setEnabled(False)
            self.login_thread.start()
            print("Login Thread Started")

    def on_handle_login_finished(self):
        self.ui.pb_logIn.setEnabled(True)

    def handle_otp_signal(self, otp_tuple):
        print(otp_tuple)
        self.otp_signal.emit(otp_tuple)

    def handle_error_signal(self, error):
        self.ui.le_status.setText(error)
        self.ui.le_status.setVisible(True)

    def eventFilter(self, obj, event):
        if event.type() == QtCore.QEvent.Type.KeyPress and event.key() == QtCore.Qt.Key.Key_Return:
            self.startLoginThread()
            return True
        return super().eventFilter(obj, event)

    def custom_box(self):
        message_box = CustomMessageBox(self, main_app=self.main_app)
        if message_box.notifyAction("Confirm", "Are you sure?","loading1.gif"):
            print("ngi")
