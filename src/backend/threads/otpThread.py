from PyQt6.QtCore import QThread, pyqtSignal


class OTPThread(QThread):
    finished = pyqtSignal()

    def __init__(self, otp_form):
        super().__init__()
        self.otp_form = otp_form

    def run(self):
        self.otp_form.processOTP()
        self.finished.emit()
