from PyQt6.QtCore import QThread, pyqtSignal
import requests
import hashlib
from src.backend.database.login.auth import check_db_for_user, login_user, login_attempt, otp_attempts
from src.backend.database.login.record_logins import record_login_attempt, record_session, activity_log
from src.backend.controllers.controller_utility import generate_session_id


class LoginThread(QThread):
    finished = pyqtSignal()
    otp_signal = pyqtSignal(tuple)
    error_signal = pyqtSignal(str)

    def __init__(self, login_form):
        super().__init__()
        self.login_form = login_form

    def run(self):
        self.handleLogin()
        self.finished.emit()

    def handleLogin(self):
        if self.login_form.ui.le_username.text() == "" or self.login_form.ui.le_pass.text() == "":
            print("Please fill in all fields")
            self.error_signal.emit("Empty Fields")
            return

        username = self.login_form.ui.le_username.text()
        password = self.login_form.ui.le_pass.text()
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        ip = requests.get('https://api64.ipify.org').text

        user_exists = check_db_for_user(username)

        if user_exists is None:
            print("No user found")
            self.error_signal.emit("No User Found")
            self.login_form.ui.le_pass.clear()
            return

        user = login_user(username, hashed_password)
        wrong_attempts = login_attempt(user_exists[0])

        if wrong_attempts is not None and wrong_attempts[1] >= 3:
            self.error_signal.emit("Too Many Wrong Attempts")
            self.login_form.ui.le_pass.clear()
            return

        if user is None:
            self.login_form.login_id = record_login_attempt(user_exists[0], False, ip)
            print(str(self.login_form.login_id) + "" + "NGI LOGIN")
            self.error_signal.emit("Wrong Password")
            print("Wrong password")
            self.login_form.ui.le_pass.clear()
            return

        otp_count = otp_attempts(user[0])

        if user[3] and otp_count is not None and otp_count >= 3:
            print("Too many OTP attempts")
            self.error_signal.emit("Too Many OTP Attempts")
            self.login_form.ui.le_pass.clear()
            return

        self.login_form.login_id = record_login_attempt(user[0], True, ip)
        self.login_form.ui.le_username.clear()
        self.login_form.ui.le_pass.clear()
        self.login_form.ui.le_username.setFocus()
        self.login_form.user = user
        self.check_otp()

    def check_otp(self):
        if self.login_form.user[3]:
            otp_tuple = self.login_form.user + (self.login_form.login_id,)
            self.otp_signal.emit(otp_tuple)
            self.login_form.main_app.setCurrentWidget('otp')
            return
        session_id = generate_session_id()
        record_session(session_id, self.login_form.user[0], self.login_form.login_id)
        activity_log(self.login_form.user[0], "Log In", "Account", "Login Attempt from", session_id)
        info = self.login_form.user + (session_id,)
        self.login_form.main_app.mainLoggedIn.emit(info)
        self.login_form.main_app.setCurrentWidget(self.login_form.user[2])
