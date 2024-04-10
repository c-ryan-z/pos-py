from PyQt6.QtCore import QThread, pyqtSignal, QMutex


class OTPThread(QThread):
    finished = pyqtSignal()

    def __init__(self, otp_form):
        super().__init__()
        self.otp_form = otp_form
        self.mutex = QMutex()

    def run(self):
        self.mutex.lock()
        self.otp_form.processOTP()
        self.finished.emit()
        self.mutex.unlock()
