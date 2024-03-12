from PyQt6 import QtWidgets as Qtw
from PyQt6 import QtCore
import hashlib

from src.frontend.otpForm import Ui_OTP

from src.backend.mailer import two_factor_auth
from src.backend.database.auth import (create_codes, verifyLoginOtp, check_user_otp, increment_otp_attempts,
                                       setOtpAttempt)
from src.backend.database.record_logins import record_session
from src.backend.controllers.Utility import generate_code, generate_session_id
from src.backend.threads.otpThread import OTPThread


class OTPForm(Qtw.QWidget):
    OtpVerified = QtCore.pyqtSignal(str)

    def __init__(self, main_app, login_form):
        super().__init__()
        self.ui = Ui_OTP()
        self.ui.setupUi(self)
        self.main = main_app
        self.login_form = login_form
        self.user = None

        self.ui.pb_otp.clicked.connect(self.handleOTP)
        self.ui.pb_otp.setEnabled(False)

        self.login_form.userLoggedIn.connect(self.initialize_class)

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
        # todo: Implementing the loading animation
        self.ui.pb_otp.setEnabled(True)

    def handleOTP(self):
        hashed_le_otp = hashlib.sha256(self.ui.le_otp.text().encode()).hexdigest()
        otp = check_user_otp(self.user[0])
        query = verifyLoginOtp(self.user[0], hashed_le_otp)

        if otp is None:
            print("OTP EXPIRED // RESEND CODE?")
            return

        if otp[0] >= 3:
            print("Too many attempts LIMIT? OR RESEND CODE?")
            return

        if query is None:
            self.ui.le_otp.clear()
            print("Invalid OTP")
            increment_otp_attempts(self.user[0])
            return

        self.OtpVerified.emit(self.user[2])
        login_id = setOtpAttempt(self.user[0])

        session_id = generate_session_id()
        record_session(session_id, self.user[0], login_id)

