from PyQt6 import QtWidgets as Qtw
import hashlib

from src.backend.mailer import two_factor_auth
from src.frontend.login.otpForm import Ui_OTP

from src.backend.controllers.__customWidget.CustomMessageBox import CustomMessageBox
from src.backend.database.login.auth import (create_codes, verify_login_otp, check_user_otp, increment_otp_attempts,
                                             otp_attempt_true)
from src.backend.database.login.record_logins import record_session, activity_log
from src.backend.controllers.controller_utility import generate_code, generate_session_id
from src.backend.threads.login.otpThread import OTPThread


class OTPForm(Qtw.QWidget):

    def __init__(self, main_app, login_form):
        super().__init__()
        self.ui = Ui_OTP()
        self.ui.setupUi(self)
        self.main = main_app
        self.login_form = login_form
        self.user = None

        self.ui.pb_otp.clicked.connect(self.handleOTP)
        self.ui.le_otp.setTextMargins(20, 25, 20, 25)
        self.ui.le_otp.setStyleSheet("""
            QLineEdit {
                border-radius: 16px;
            }
        """)
        self.ui.pb_otp.setEnabled(False)

        self.login_form.otp_signal.connect(self.initialize_class)

        self.otp_thread = OTPThread(self)
        self.otp_thread.finished.connect(self.on_processOTP_finished)

    def initialize_class(self, user):
        self.user = user
        self.otp_thread.start()

    def processOTP(self):
        code = generate_code()
        # two_factor_auth(self.user[1], self.user[4], code)
        print(code)
        hashed_code = hashlib.sha256(code.encode()).hexdigest()
        create_codes(hashed_code, self.user[0], 'OTP')

    def on_processOTP_finished(self):
        message = CustomMessageBox(self, self.main)
        if message.notifyAction("Email Sent", "Please check your email for the OTP code", "email.gif"):
            print("Acknowledged")
        self.ui.pb_otp.setEnabled(True)

    def handleOTP(self):
        hashed_le_otp = hashlib.sha256(self.ui.le_otp.text().encode()).hexdigest()
        otp = check_user_otp(self.user[0])

        if otp is None:
            print("OTP EXPIRED // RESEND CODE?")
            return

        if otp[0] >= 3:
            print("Too many attempts LIMIT? OR RESEND CODE?")
            return

        query = verify_login_otp(self.user[0], hashed_le_otp)
        if query is None:
            self.ui.le_otp.clear()
            print("Invalid OTP")
            increment_otp_attempts(self.user[0])
            return

        otp_attempt_true(self.user[5])
        session_id = generate_session_id()
        print(str(self.user[5]) + " OTP SUCCESS")
        record_session(session_id, self.user[0], self.user[5])
        activity_log(self.user[0], "Log In", "Account", "Login Attempt from", session_id)

        info = self.user + (session_id, )

        self.main.setCurrentWidget(self.user[2])
        self.main.mainLoggedIn.emit(info)
        self.ui.le_otp.clear()
        self.ui.pb_otp.setEnabled(False)
        self.user = None
