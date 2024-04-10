from PyQt6 import QtWidgets as Qtw

import hashlib

from src.frontend.login.pass_reset import Ui_Form
from src.backend.controllers.controller_utility import generate_code
from src.backend.database.login.forgot_pw import (verify_email, insert_reset_code,
                                                  check_code, change_password, rate_limit, verify_code,
                                                  increment_code_attempts, record_successful_reset)
from src.backend.mailer import password_reset


class PasswordReset(Qtw.QWidget):

    def __init__(self, main_app):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.main_app = main_app
        self.user_id = None

        self.ui.pb_back.clicked.connect(self.set_page)
        self.ui.pb_email.clicked.connect(self.send_email)
        self.ui.pb_code.clicked.connect(self.verify_code)
        self.ui.pb_password.clicked.connect(self.reset_password)

    def set_page(self):
        index = self.ui.sw_page.currentIndex()

        if index == 0:
            self.main_app.setCurrentWidget('login')
        else:
            self.ui.sw_page.setCurrentIndex(index - 1)

    def send_email(self):
        email = self.ui.le_email.text()
        verify = verify_email(email)

        if verify is None:
            # todo show error
            return

        limit = rate_limit(email)
        if limit[0] > 3:
            # todo show error
            return

        self.user_id = verify[0]
        code = generate_code()

        hash_code = hashlib.sha256(code.encode()).hexdigest()
        insert_reset_code(hash_code, verify[0], 'RESET')

        print("Code: ", code)
        # password_reset(verify[1], email, code)
        self.ui.sw_page.setCurrentIndex(1)

    def verify_code(self):
        code = self.ui.le_code.text()
        hash_code = hashlib.sha256(code.encode()).hexdigest()
        code_db = check_code(hash_code, self.user_id, 'RESET')

        if code_db is None:
            print("OTP EXPIRED // RESEND CODE?")
            return

        if code_db[0] >= 3:
            print("Too many attempts LIMIT? OR RESEND CODE?")
            return

        query_db = verify_code(self.user_id, hash_code)
        if query_db is None:
            print("Invalid OTP")
            self.ui.le_code.clear()
            increment_code_attempts(self.user_id, 'RESET')
            return

        self.ui.sw_page.setCurrentIndex(2)

    def reset_password(self):
        password = self.ui.le_password.text()
        verify = self.ui.le_verify.text()

        if password != verify:
            # todo show error
            return

        hashed_pw = hashlib.sha256(password.encode()).hexdigest()
        change_password(self.user_id, hashed_pw)
        record_successful_reset(self.user_id)
        self.main_app.setCurrentWidget('login')
